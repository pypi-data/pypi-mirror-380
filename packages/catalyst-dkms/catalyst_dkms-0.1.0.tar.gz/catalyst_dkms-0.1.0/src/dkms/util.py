"""Utility functions for DKMS."""

import hashlib
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import structlog

# Configure structured logging
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(20),  # INFO level
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(file=sys.stdout),
    cache_logger_on_first_use=True,
)


def get_logger(name: str) -> Any:
    """Get a structured logger instance."""
    return structlog.get_logger(name)


def compute_hash(content: str | bytes) -> str:
    """Compute SHA256 hash of content."""
    if isinstance(content, str):
        content = content.encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def utc_now() -> datetime:
    """Get current UTC datetime."""
    return datetime.now(UTC)


def read_file(path: Path) -> str:
    """Read file content as text."""
    return path.read_text(encoding="utf-8")


def count_lines(text: str) -> int:
    """Count lines in text."""
    return len(text.splitlines())


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def format_metrics(metrics: dict[str, Any]) -> str:
    """Format metrics as JSON string."""
    return json.dumps(metrics, indent=2)
