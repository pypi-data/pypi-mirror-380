"""Resource monitoring and adaptive concurrency."""

import os

from src.dkms.config import ResourceConfig


class ResourceMonitor:
    """Monitor and manage resource usage."""

    def __init__(self, config: ResourceConfig):
        """Initialize resource monitor."""
        self.config = config
        self.cpu_count = os.cpu_count() or 1

    def get_thread_pool_size(self) -> int:
        """
        Calculate optimal thread pool size.

        For MVP: clamp to available CPU count minus 1.
        """
        optimal = max(self.cpu_count - 1, 1)
        return max(self.config.min_threads, min(optimal, self.config.max_threads))
