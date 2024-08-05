import json
import logging

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def parse_json(response):
    """
    Safely parse JSON from the response.
    """
    try:
        return response.json()
    except json.JSONDecodeError:
        logger.error("Failed to decode JSON response")
        return {}

def validate_steam_id(steam_id):
    """
    Validate if the provided Steam ID is in the correct format.
    """
    if isinstance(steam_id, str) and steam_id.isdigit():
        return True
    logger.warning(f"Invalid Steam ID: {steam_id}")
    return False

def country_code_to_flag(country_code):
    """
    Convert a country code to a Unicode flag emoji.
    """
    country_code = country_code.upper()
    return ''.join(chr(0x1F1E6 + ord(char) - ord('A')) for char in country_code) if country_code else 'No flag/bandera'

def handle_api_error(response):
    """
    Handle API errors by logging and raising an exception.
    """
    if response.status_code != 200:
        logger.error(f"API request failed with status code {response.status_code}: {response.text}")
        response.raise_for_status()

def format_steam_url(steam_id):
    """
    Format the Steam URL from a Steam ID.
    """
    return f"https://steamcommunity.com/profiles/{steam_id}"
