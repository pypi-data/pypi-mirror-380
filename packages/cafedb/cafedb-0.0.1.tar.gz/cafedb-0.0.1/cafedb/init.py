# cafedb/__init__.py

"""
CafeDB - A lightweight, Python-native, JSONL-based database with set-indexed querying.
Provides easy-to-use insert, query, update, and delete operations with Python-native types.
"""

from .cafedb import CafeDB  # core database class

__all__ = ["CafeDB"]
__version__ = "0.0.1"