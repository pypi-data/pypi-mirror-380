"""SQLAlchemy models for DKMS."""

import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import JSON, Boolean, DateTime, Index, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import CHAR, TypeDecorator

try:
    from pgvector.sqlalchemy import Vector
    VECTOR_TYPE: Any = Vector(384)
except ImportError:
    # Fallback for testing with SQLite
    VECTOR_TYPE = JSON


class GUID(TypeDecorator):
    """Platform-independent GUID type.
    Uses PostgreSQL's UUID type, otherwise uses CHAR(32), storing as stringified hex values.
    """
    impl = CHAR
    cache_ok = True

    def load_dialect_impl(self, dialect: Any) -> Any:
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(PG_UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value: Any, dialect: Any) -> str | None:
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return str(uuid.UUID(value)).replace('-', '')
            else:
                return str(value).replace('-', '')

    def process_result_value(self, value: Any, dialect: Any) -> uuid.UUID | None:
        if value is None:
            return value
        else:
            if not isinstance(value, uuid.UUID):
                if len(str(value)) == 32:
                    # SQLite format: add dashes
                    value = str(value)
                    return uuid.UUID(f"{value[:8]}-{value[8:12]}-{value[12:16]}-{value[16:20]}-{value[20:]}")
                else:
                    return uuid.UUID(value)
            return value


class Base(DeclarativeBase):
    """Base class for all models."""

    pass


class Document(Base):
    """Document model."""

    __tablename__ = "documents"

    doc_id: Mapped[uuid.UUID] = mapped_column(
        GUID(), primary_key=True, default=uuid.uuid4
    )
    content_hash: Mapped[str] = mapped_column(Text, unique=True, nullable=False, index=True)
    source_path: Mapped[str] = mapped_column(Text, nullable=False)
    mime_hint: Mapped[str | None] = mapped_column(Text, nullable=True)
    byte_size: Mapped[int] = mapped_column(Integer, nullable=False)
    line_count: Mapped[int] = mapped_column(Integer, nullable=False)
    word_count: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    pii_scrubbed: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    pii_report: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    raw_text: Mapped[str] = mapped_column(Text, nullable=False)


class DocEmbedding(Base):
    """Document embedding model."""

    __tablename__ = "doc_embeddings"

    doc_id: Mapped[uuid.UUID] = mapped_column(GUID(), primary_key=True, nullable=False)
    provider: Mapped[str] = mapped_column(String(100), primary_key=True, nullable=False)
    dim: Mapped[int] = mapped_column(Integer, nullable=False)
    vector: Mapped[Any] = mapped_column(VECTOR_TYPE, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    __table_args__ = (Index("idx_doc_embeddings_vector", "vector", postgresql_using="ivfflat"),)


class DocLabel(Base):
    """Document label model."""

    __tablename__ = "doc_labels"

    doc_id: Mapped[uuid.UUID] = mapped_column(GUID(), primary_key=True, nullable=False)
    level: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)
    label: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    confidence: Mapped[float] = mapped_column(Numeric(5, 4), nullable=False)
    provider: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class Run(Base):
    """Run tracking model."""

    __tablename__ = "runs"

    run_id: Mapped[uuid.UUID] = mapped_column(
        GUID(), primary_key=True, default=uuid.uuid4
    )
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    config_jsonb: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    metrics_jsonb: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)


class Checkpoint(Base):
    """Checkpoint model for resumable runs."""

    __tablename__ = "checkpoints"

    run_id: Mapped[uuid.UUID] = mapped_column(GUID(), primary_key=True, nullable=False)
    cursor: Mapped[str] = mapped_column(Text, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
