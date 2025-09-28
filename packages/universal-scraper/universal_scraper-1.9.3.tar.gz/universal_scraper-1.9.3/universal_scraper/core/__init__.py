"""
Core functionality for Universal Scraper.

This module contains the core components for web scraping:
- html_fetcher: HTML content fetching
- html_cleaner: HTML cleaning and preprocessing
- data_extractor: AI-powered data extraction
- code_cache: Caching system for generated code
"""

from .html_fetcher import HtmlFetcher
from .html_cleaner import HtmlCleaner
from .data_extractor import DataExtractor
from .code_cache import CodeCache

__all__ = ["HtmlFetcher", "HtmlCleaner", "DataExtractor", "CodeCache"]
