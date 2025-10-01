"""File format detection for DKMS."""

import json
from pathlib import Path
from typing import Literal

FileFormat = Literal["txt", "json", "jsonl", "unknown"]


def detect_format(path: Path) -> FileFormat:
    """Detect file format based on extension and content sniffing."""
    ext = path.suffix.lower()

    if ext == ".jsonl":
        return "jsonl"
    elif ext == ".json":
        return "json"
    elif ext == ".txt":
        return "txt"

    # Try to detect by content
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
        if not content.strip():
            return "unknown"

        # Try JSON parsing
        try:
            json.loads(content)
            return "json"
        except json.JSONDecodeError:
            pass

        # Check if JSONL (each line is JSON)
        lines = content.strip().split("\n")
        if lines and all(is_json_line(line) for line in lines[:10] if line.strip()):
            return "jsonl"

        # Default to text
        return "txt"
    except Exception:
        return "unknown"


def is_json_line(line: str) -> bool:
    """Check if a line is valid JSON."""
    try:
        json.loads(line)
        return True
    except json.JSONDecodeError:
        return False


def parse_content(path: Path, format_type: FileFormat) -> str:
    """Parse file content based on format and return as text."""
    content = path.read_text(encoding="utf-8")

    if format_type == "json":
        # Pretty print JSON
        try:
            data = json.loads(content)
            return json.dumps(data, indent=2)
        except json.JSONDecodeError:
            return content
    elif format_type == "jsonl":
        # Parse each line and join
        lines = []
        for line in content.split("\n"):
            if line.strip():
                try:
                    data = json.loads(line)
                    lines.append(json.dumps(data))
                except json.JSONDecodeError:
                    lines.append(line)
        return "\n".join(lines)
    else:
        return content
