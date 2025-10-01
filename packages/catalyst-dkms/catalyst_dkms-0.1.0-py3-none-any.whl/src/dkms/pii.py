"""PII scrubbing module (stub implementation)."""

import re

# Simple regex patterns for PII detection
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
PHONE_PATTERN = re.compile(
    r"(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\d{3}[-.\s]\d{3}[-.\s]\d{4}"
)


def scrub(text: str, patterns: list[str] | None = None) -> tuple[str, dict[str, int]]:
    """
    Scrub PII from text (stub implementation).

    Args:
        text: Input text
        patterns: List of pattern types to scrub (email, phone)

    Returns:
        Tuple of (scrubbed_text, report)
    """
    if patterns is None:
        patterns = ["email", "phone"]

    report: dict[str, int] = {}
    scrubbed = text

    if "email" in patterns:
        emails = EMAIL_PATTERN.findall(text)
        report["emails_found"] = len(emails)
        scrubbed = EMAIL_PATTERN.sub("[EMAIL_REDACTED]", scrubbed)

    if "phone" in patterns:
        phones = PHONE_PATTERN.findall(text)
        report["phones_found"] = len(phones)
        scrubbed = PHONE_PATTERN.sub("[PHONE_REDACTED]", scrubbed)

    report["total_redactions"] = report.get("emails_found", 0) + report.get("phones_found", 0)

    return scrubbed, report
