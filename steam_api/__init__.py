"""
steam_api - A Python library for interacting with the Steam API.
"""

from .steam_api import SteamAPI
from .utils import parse_json, validate_steam_id, country_code_to_flag, handle_api_error, format_steam_url

__all__ = [
    'SteamAPI',
    'parse_json',
    'validate_steam_id',
    'country_code_to_flag',
    'handle_api_error',
    'format_steam_url',
]

__version__ = '0.1'
__author__ = 'Your Name'
__email__ = 'your.email@example.com'
__url__ = 'https://github.com/yourusername/yourrepository'
