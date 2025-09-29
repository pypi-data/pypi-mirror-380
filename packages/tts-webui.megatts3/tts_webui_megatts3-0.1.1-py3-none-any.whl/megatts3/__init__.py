# Public API for MegaTTS3
from .infer_cli import MegaTTS3DiTInfer
from .download import download_checkpoints

__all__ = ["MegaTTS3DiTInfer", "download_checkpoints"]
