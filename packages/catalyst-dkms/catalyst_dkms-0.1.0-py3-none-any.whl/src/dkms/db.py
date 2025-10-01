"""Database session and helpers for DKMS."""

from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.dkms.config import DKMSConfig
from src.dkms.models import Base

_engine = None
_session_factory = None


def init_db(config: DKMSConfig) -> None:
    """Initialize database engine and session factory."""
    global _engine, _session_factory

    # Different config for SQLite vs PostgreSQL
    if config.database.url.startswith("sqlite"):
        _engine = create_engine(
            config.database.url,
            echo=False,
        )
    else:
        _engine = create_engine(
            config.database.url,
            pool_size=config.database.pool_size,
            max_overflow=config.database.max_overflow,
            echo=False,
        )
    _session_factory = sessionmaker(bind=_engine, expire_on_commit=False)


def create_tables() -> None:
    """Create all tables (for testing only, use Alembic in production)."""
    if _engine is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    Base.metadata.create_all(_engine)


@contextmanager
def get_session() -> Generator[Session, None, None]:
    """Get a database session context manager."""
    if _session_factory is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    session = _session_factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
