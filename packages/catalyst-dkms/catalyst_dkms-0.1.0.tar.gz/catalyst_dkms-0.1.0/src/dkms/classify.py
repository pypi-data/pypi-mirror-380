"""Classification provider interface and stub implementation."""

import hashlib
import random

from src.dkms.config import ClassificationConfig


class Label:
    """Classification label with confidence."""

    def __init__(self, level: str, label: str, confidence: float, provider: str):
        """Initialize label."""
        self.level = level
        self.label = label
        self.confidence = confidence
        self.provider = provider


class ClassificationProvider:
    """Base classification provider interface."""

    def __init__(self, config: ClassificationConfig):
        """Initialize provider."""
        self.config = config
        self.levels = config.levels

    def label(self, text: str) -> list[Label]:
        """Generate labels for text."""
        raise NotImplementedError


class LocalClassificationProvider(ClassificationProvider):
    """
    Local stub classification provider.

    Uses simple keyword matching and deterministic confidence scores.
    """

    # Simple keyword-based rules
    DOMAIN_KEYWORDS: dict[str, list[str]] = {
        "technical": ["code", "function", "class", "import", "def", "return", "error", "bug"],
        "business": ["revenue", "sales", "customer", "market", "strategy", "profit"],
        "legal": ["contract", "agreement", "law", "regulation", "compliance", "clause"],
        "medical": ["patient", "diagnosis", "treatment", "symptoms", "medical", "health"],
        "general": [],  # default
    }

    CATEGORY_KEYWORDS: dict[str, list[str]] = {
        "documentation": ["readme", "guide", "manual", "tutorial", "howto"],
        "data": ["json", "csv", "table", "record", "field", "database"],
        "communication": ["email", "message", "letter", "memo", "note"],
        "report": ["analysis", "summary", "findings", "report", "results"],
        "other": [],  # default
    }

    SUBCATEGORY_KEYWORDS: dict[str, list[str]] = {
        "structured": ["json", "xml", "yaml", "csv", "table"],
        "unstructured": ["text", "paragraph", "prose", "narrative"],
        "mixed": ["format", "mixed", "combined"],
        "unknown": [],  # default
    }

    def __init__(self, config: ClassificationConfig, seed: int = 42):
        """Initialize local provider."""
        super().__init__(config)
        self.seed = seed

    def label(self, text: str) -> list[Label]:
        """Generate labels based on keyword matching."""
        text_lower = text.lower()
        labels: list[Label] = []

        # Deterministic confidence based on text hash
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        seed_value = int(text_hash[:8], 16) ^ self.seed
        rng = random.Random(seed_value)

        # Domain
        domain = self._match_keywords(text_lower, self.DOMAIN_KEYWORDS, "general")
        confidence = rng.uniform(0.7, 0.9)
        labels.append(Label("domain", domain, round(confidence, 4), "local"))

        # Category
        category = self._match_keywords(text_lower, self.CATEGORY_KEYWORDS, "other")
        confidence = rng.uniform(0.6, 0.85)
        labels.append(Label("category", category, round(confidence, 4), "local"))

        # Subcategory
        subcategory = self._match_keywords(text_lower, self.SUBCATEGORY_KEYWORDS, "unknown")
        confidence = rng.uniform(0.5, 0.8)
        labels.append(Label("subcategory", subcategory, round(confidence, 4), "local"))

        return labels

    def _match_keywords(self, text: str, keyword_map: dict[str, list[str]], default: str) -> str:
        """Match text against keyword groups."""
        best_match = default
        best_count = 0

        for label, keywords in keyword_map.items():
            if not keywords:  # Skip empty keyword lists (defaults)
                continue
            count = sum(1 for kw in keywords if kw in text)
            if count > best_count:
                best_count = count
                best_match = label

        return best_match


def get_provider(config: ClassificationConfig) -> ClassificationProvider:
    """Get classification provider based on config."""
    if config.provider == "local":
        return LocalClassificationProvider(config)
    else:
        raise ValueError(f"Unknown classification provider: {config.provider}")
