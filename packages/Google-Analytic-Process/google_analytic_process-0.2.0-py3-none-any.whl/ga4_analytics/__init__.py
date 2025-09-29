"""
GA4 Analytics API Client

A simple library for making raw Google Analytics 4 API calls.
All data processing should be handled in the consuming application.
"""

from .processor import GA4Client

__version__ = "0.2.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = ["GA4Client"]