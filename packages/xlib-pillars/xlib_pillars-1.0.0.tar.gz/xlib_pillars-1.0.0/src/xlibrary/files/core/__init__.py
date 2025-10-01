"""Core components for the files pillar."""

from .manager import FileManager
from .operations import FileOperations
from .deduplication import DuplicateFinder
from .compression import CompressionManager
from .types import *

__all__ = [
    "FileManager",
    "FileOperations",
    "DuplicateFinder",
    "CompressionManager"
]