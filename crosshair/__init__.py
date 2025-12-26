"""
Crosshair Module
Provides crosshair database functionality for the UI
"""

from .scraper import (
    fetch_crosshairs,
    load_crosshairs,
    search_crosshairs,
    get_top_crosshairs
)

__all__ = [
    "fetch_crosshairs",
    "load_crosshairs", 
    "search_crosshairs",
    "get_top_crosshairs"
]
