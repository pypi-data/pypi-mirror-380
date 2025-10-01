"""Configuration management for DKMS with precedence: CLI > ENV > YAML."""

from pathlib import Path
from typing import Any

import yaml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    """Database configuration."""

    url: str = Field(default="postgresql://dkms:dkms@localhost:5432/dkms")
    pool_size: int = Field(default=5)
    max_overflow: int = Field(default=10)

    model_config = SettingsConfigDict(env_prefix="DKMS_DB_")


class IngestConfig(BaseSettings):
    """Ingest configuration."""

    batch_size: int = Field(default=64)
    safe_mode: bool = Field(default=True)
    supported_extensions: list[str] = Field(default=[".txt", ".json", ".jsonl"])

    model_config = SettingsConfigDict(env_prefix="DKMS_INGEST_")


class ResourceConfig(BaseSettings):
    """Resource management configuration."""

    min_threads: int = Field(default=1)
    max_threads: int = Field(default=4)

    model_config = SettingsConfigDict(env_prefix="DKMS_RESOURCES_")


class EmbeddingsConfig(BaseSettings):
    """Embeddings configuration."""

    provider: str = Field(default="local")
    dimension: int = Field(default=384)

    model_config = SettingsConfigDict(env_prefix="DKMS_EMBEDDINGS_")


class ClassificationConfig(BaseSettings):
    """Classification configuration."""

    provider: str = Field(default="local")
    levels: list[str] = Field(default=["domain", "category", "subcategory"])

    model_config = SettingsConfigDict(env_prefix="DKMS_CLASSIFICATION_")


class PIIConfig(BaseSettings):
    """PII scrubbing configuration."""

    enabled: bool = Field(default=True)
    patterns: list[str] = Field(default=["email", "phone"])

    model_config = SettingsConfigDict(env_prefix="DKMS_PII_")


class LoggingConfig(BaseSettings):
    """Logging configuration."""

    level: str = Field(default="INFO")
    format: str = Field(default="json")

    model_config = SettingsConfigDict(env_prefix="DKMS_LOGGING_")


class DKMSConfig(BaseSettings):
    """Main DKMS configuration."""

    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    ingest: IngestConfig = Field(default_factory=IngestConfig)
    resources: ResourceConfig = Field(default_factory=ResourceConfig)
    embeddings: EmbeddingsConfig = Field(default_factory=EmbeddingsConfig)
    classification: ClassificationConfig = Field(default_factory=ClassificationConfig)
    pii: PIIConfig = Field(default_factory=PIIConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)

    model_config = SettingsConfigDict(env_prefix="DKMS_")

    @classmethod
    def from_yaml(cls, yaml_path: Path | None = None) -> "DKMSConfig":
        """Load configuration from YAML file with env var overrides."""
        if yaml_path is None:
            yaml_path = Path(__file__).parent.parent.parent / "configs" / "dkms.yaml"

        config_dict: dict[str, Any] = {}
        if yaml_path.exists():
            with open(yaml_path) as f:
                config_dict = yaml.safe_load(f) or {}

        # Create sub-configs with YAML data, env vars will override
        return cls(
            database=DatabaseConfig(**config_dict.get("database", {})),
            ingest=IngestConfig(**config_dict.get("ingest", {})),
            resources=ResourceConfig(**config_dict.get("resources", {})),
            embeddings=EmbeddingsConfig(**config_dict.get("embeddings", {})),
            classification=ClassificationConfig(**config_dict.get("classification", {})),
            pii=PIIConfig(**config_dict.get("pii", {})),
            logging=LoggingConfig(**config_dict.get("logging", {})),
        )


def get_config(yaml_path: Path | None = None) -> DKMSConfig:
    """Get configuration with proper precedence."""
    return DKMSConfig.from_yaml(yaml_path)
