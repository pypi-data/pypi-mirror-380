"""CLI for DKMS using Click."""

import json
from pathlib import Path

import click
from sqlalchemy import func, select

from src.dkms.config import get_config
from src.dkms.db import get_session, init_db
from src.dkms.ingest import IngestManager, resume_ingest
from src.dkms.models import DocLabel, Document


@click.group()
def cli() -> None:
    """DKMS - Domain Knowledge Management System preprocessing toolset."""
    pass


@cli.command()
@click.option(
    "--input",
    "input_path",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help="Input file or directory path",
)
@click.option(
    "--safe",
    default=True,
    type=bool,
    help="Enable PII scrubbing (default: true)",
)
@click.option(
    "--batch",
    "batch_size",
    default=64,
    type=int,
    help="Batch size for processing (default: 64)",
)
@click.option(
    "--config",
    "config_path",
    type=click.Path(exists=True, path_type=Path),
    help="Path to config YAML file",
)
def ingest(
    input_path: Path,
    safe: bool,
    batch_size: int,
    config_path: Path | None,
) -> None:
    """Ingest documents from input path."""
    # Load config
    config = get_config(config_path)

    # Override with CLI flags
    if safe is not None:
        config.ingest.safe_mode = safe
    if batch_size is not None:
        config.ingest.batch_size = batch_size

    # Initialize database
    init_db(config)

    # Run ingestion
    manager = IngestManager(config)
    metrics = manager.ingest(input_path, safe, batch_size)

    # Print summary as JSON
    summary = {
        "status": "interrupted" if manager.should_stop else "success",
        "processed": metrics["files_processed"],
        "skipped": metrics["files_skipped"],
        "errors": metrics["files_error"],
        "elapsed_ms": metrics.get("elapsed_ms", 0),
    }
    click.echo(json.dumps(summary))


@cli.command()
@click.option(
    "--config",
    "config_path",
    type=click.Path(exists=True, path_type=Path),
    help="Path to config YAML file",
)
def resume(config_path: Path | None) -> None:
    """Resume from last checkpoint."""
    config = get_config(config_path)
    init_db(config)

    result = resume_ingest(config)
    click.echo(json.dumps(result))


@cli.command()
@click.option(
    "--config",
    "config_path",
    type=click.Path(exists=True, path_type=Path),
    help="Path to config YAML file",
)
def stats(config_path: Path | None) -> None:
    """Print statistics and metrics."""
    config = get_config(config_path)
    init_db(config)

    with get_session() as session:
        # Document count
        doc_count = session.execute(select(func.count(Document.doc_id))).scalar_one()

        # Label counts
        label_counts = session.execute(
            select(DocLabel.label, func.count(DocLabel.doc_id))
            .group_by(DocLabel.label)
            .order_by(func.count(DocLabel.doc_id).desc())
        ).all()

    stats_output = {
        "total_documents": doc_count,
        "labels": dict(label_counts),  # type: ignore[arg-type]
    }

    click.echo(json.dumps(stats_output, indent=2))


if __name__ == "__main__":
    cli()
