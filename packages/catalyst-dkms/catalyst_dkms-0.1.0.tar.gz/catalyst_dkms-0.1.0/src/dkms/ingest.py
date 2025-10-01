"""Ingest module for DKMS with graceful shutdown."""

import signal
import uuid
from pathlib import Path
from typing import Any

from sqlalchemy import select

from src.dkms import classify, embeddings, pii
from src.dkms.config import DKMSConfig
from src.dkms.db import get_session
from src.dkms.io_detect import detect_format, parse_content
from src.dkms.models import Checkpoint, DocEmbedding, DocLabel, Document, Run
from src.dkms.util import compute_hash, count_lines, count_words, get_logger, utc_now

logger = get_logger(__name__)


class IngestManager:
    """Manage document ingestion with graceful shutdown."""

    def __init__(self, config: DKMSConfig):
        """Initialize ingest manager."""
        self.config = config
        self.should_stop = False
        self.current_run_id: uuid.UUID | None = None
        self.metrics: dict[str, Any] = {
            "files_processed": 0,
            "files_skipped": 0,
            "files_error": 0,
            "bytes_processed": 0,
        }

        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _signal_handler(self, signum: int, frame: Any) -> None:
        """Handle shutdown signals gracefully."""
        logger.info("shutdown_signal_received", signal=signum)
        self.should_stop = True

    def ingest(self, input_path: Path, safe: bool = True, batch_size: int = 64) -> dict[str, Any]:
        """
        Ingest documents from input path.

        Args:
            input_path: Path to file or directory
            safe: Enable PII scrubbing
            batch_size: Batch size for processing

        Returns:
            Summary metrics
        """
        start_time = utc_now()

        # Create run record
        with get_session() as session:
            run = Run(
                run_id=uuid.uuid4(),
                started_at=start_time,
                status="running",
                config_jsonb={
                    "input_path": str(input_path),
                    "safe": safe,
                    "batch_size": batch_size,
                },
            )
            session.add(run)
            session.flush()
            self.current_run_id = run.run_id

        logger.info("ingest_started", run_id=str(self.current_run_id), path=str(input_path))

        # Collect files
        files = self._collect_files(input_path)
        logger.info("files_collected", count=len(files))

        # Initialize providers
        emb_provider = embeddings.get_provider(self.config.embeddings)
        cls_provider = classify.get_provider(self.config.classification)

        # Process files
        for file_path in files:
            if self.should_stop:
                logger.info("shutdown_requested", checkpoint_written=True)
                self._write_checkpoint(str(file_path))
                break

            try:
                self._process_file(file_path, safe, emb_provider, cls_provider)
            except Exception as e:
                logger.error("file_processing_error", path=str(file_path), error=str(e))
                self.metrics["files_error"] += 1

        # Finalize run
        end_time = utc_now()
        elapsed_ms = int((end_time - start_time).total_seconds() * 1000)
        self.metrics["elapsed_ms"] = elapsed_ms

        status = "interrupted" if self.should_stop else "completed"
        with get_session() as session:
            run_obj = session.get(Run, self.current_run_id)
            if run_obj is not None:
                run_obj.finished_at = end_time
                run_obj.status = status
                run_obj.metrics_jsonb = self.metrics

        logger.info("ingest_finished", status=status, metrics=self.metrics)
        return self.metrics

    def _collect_files(self, path: Path) -> list[Path]:
        """Collect files to process."""
        if path.is_file():
            return [path]

        files: list[Path] = []
        supported = self.config.ingest.supported_extensions
        for ext in supported:
            files.extend(path.glob(f"**/*{ext}"))
        return sorted(files)

    def _process_file(
        self,
        file_path: Path,
        safe: bool,
        emb_provider: embeddings.EmbeddingProvider,
        cls_provider: classify.ClassificationProvider,
    ) -> None:
        """Process a single file."""
        # Detect format
        format_type = detect_format(file_path)
        if format_type == "unknown":
            logger.warning("unknown_format", path=str(file_path))
            self.metrics["files_skipped"] += 1
            return

        # Read and parse content
        content = parse_content(file_path, format_type)
        content_hash = compute_hash(content)

        # Check for duplicate
        with get_session() as session:
            existing = session.execute(
                select(Document).where(Document.content_hash == content_hash)
            ).scalar_one_or_none()

            if existing:
                logger.info("duplicate_skipped", path=str(file_path), hash=content_hash)
                self.metrics["files_skipped"] += 1
                return

        # PII scrubbing
        pii_report = None
        if safe:
            content, pii_report = pii.scrub(content, self.config.pii.patterns)

        # Compute metrics
        byte_size = file_path.stat().st_size
        line_count = count_lines(content)
        word_count = count_words(content)

        # Create document
        doc_id = uuid.uuid4()
        now = utc_now()

        with get_session() as session:
            doc = Document(
                doc_id=doc_id,
                content_hash=content_hash,
                source_path=str(file_path),
                mime_hint=format_type,
                byte_size=byte_size,
                line_count=line_count,
                word_count=word_count,
                created_at=now,
                updated_at=now,
                pii_scrubbed=safe,
                pii_report=pii_report,
                raw_text=content,
            )
            session.add(doc)

        # Generate embedding
        vector = emb_provider.embed(content)
        with get_session() as session:
            embedding = DocEmbedding(
                doc_id=doc_id,
                provider=self.config.embeddings.provider,
                dim=self.config.embeddings.dimension,
                vector=vector,
                created_at=now,
            )
            session.add(embedding)

        # Generate labels
        labels = cls_provider.label(content)
        with get_session() as session:
            for label in labels:
                doc_label = DocLabel(
                    doc_id=doc_id,
                    level=label.level,
                    label=label.label,
                    confidence=label.confidence,
                    provider=label.provider,
                    created_at=now,
                )
                session.add(doc_label)

        self.metrics["files_processed"] += 1
        self.metrics["bytes_processed"] += byte_size
        logger.info(
            "file_processed",
            path=str(file_path),
            doc_id=str(doc_id),
            format=format_type,
        )

    def _write_checkpoint(self, cursor: str) -> None:
        """Write checkpoint for resumable runs."""
        if self.current_run_id is None:
            return

        with get_session() as session:
            checkpoint = Checkpoint(
                run_id=self.current_run_id,
                cursor=cursor,
                updated_at=utc_now(),
            )
            session.merge(checkpoint)


def resume_ingest(config: DKMSConfig) -> dict[str, Any]:
    """Resume from last checkpoint."""
    with get_session() as session:
        # Find most recent incomplete run
        result = session.execute(
            select(Run).where(Run.status == "interrupted").order_by(Run.started_at.desc()).limit(1)
        ).scalar_one_or_none()

        if not result:
            logger.info("no_interrupted_run_found")
            return {"status": "no_run_to_resume"}

        # Get checkpoint
        checkpoint = session.get(Checkpoint, result.run_id)
        if not checkpoint:
            logger.info("no_checkpoint_found", run_id=str(result.run_id))
            return {"status": "no_checkpoint"}

        logger.info("resuming_from_checkpoint", cursor=checkpoint.cursor)

        # For MVP, just log - full resume implementation would continue from cursor
        return {"status": "resume_not_fully_implemented"}
