"""Embedding provider interface and stub implementation."""

import hashlib
import random

from src.dkms.config import EmbeddingsConfig


class EmbeddingProvider:
    """Base embedding provider interface."""

    def __init__(self, config: EmbeddingsConfig):
        """Initialize provider."""
        self.config = config
        self.dimension = config.dimension

    def embed(self, text: str) -> list[float]:
        """Generate embedding for text."""
        raise NotImplementedError


class LocalEmbeddingProvider(EmbeddingProvider):
    """
    Local stub embedding provider.

    Generates deterministic pseudo-random vectors based on text hash.
    Fixed seed ensures repeatability for testing.
    """

    def __init__(self, config: EmbeddingsConfig, seed: int = 42):
        """Initialize local provider."""
        super().__init__(config)
        self.seed = seed

    def embed(self, text: str) -> list[float]:
        """Generate deterministic pseudo-random embedding."""
        # Use hash of text as seed for reproducibility
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        seed_value = int(text_hash[:8], 16) ^ self.seed

        # Generate pseudo-random vector
        rng = random.Random(seed_value)
        vector = [rng.gauss(0, 1) for _ in range(self.dimension)]

        # Normalize to unit length
        magnitude = sum(x * x for x in vector) ** 0.5
        if magnitude > 0:
            vector = [x / magnitude for x in vector]

        return vector


def get_provider(config: EmbeddingsConfig) -> EmbeddingProvider:
    """Get embedding provider based on config."""
    if config.provider == "local":
        return LocalEmbeddingProvider(config)
    else:
        raise ValueError(f"Unknown embedding provider: {config.provider}")
