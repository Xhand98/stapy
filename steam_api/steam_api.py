import httpx
import os
from .utils import parse_json, validate_steam_id, country_code_to_flag, handle_api_error, format_steam_url

# Create a single AsyncClient instance
client = httpx.AsyncClient()

class SteamAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.steampowered.com"

    async def get_hours(self, user):
        if not validate_steam_id(user):
            raise ValueError("Invalid Steam ID")
        
        url = f'{self.base_url}/IPlayerService/GetOwnedGames/v1/'
        params = {'key': self.api_key, 'steamid': user, 'include_appinfo': 1, 'include_played_free_games': 1}
        
        response = await client.get(url, params=params)
        handle_api_error(response)
        data = parse_json(response)
        total_hours = sum(game.get('playtime_forever', 0) / 60 for game in data.get('response', {}).get('games', []))
        return total_hours

    async def get_steamid(self, user):
        url = f'{self.base_url}/ISteamUser/ResolveVanityURL/v0001/'
        params = {'key': self.api_key, 'vanityurl': user}
        
        response = await client.get(url, params=params)
        handle_api_error(response)
        data = parse_json(response)
        return data.get('response', {}).get('steamid')

    async def get_games(self, user):
        if not validate_steam_id(user):
            raise ValueError("Invalid Steam ID")
        
        url = f'{self.base_url}/IPlayerService/GetOwnedGames/v1/'
        params = {'key': self.api_key, 'steamid': user, 'include_appinfo': 1}
        
        response = await client.get(url, params=params)
        handle_api_error(response)
        data = parse_json(response)
        return len(data.get('response', {}).get('games', []))

    async def get_pic(self, user):
        if not validate_steam_id(user):
            raise ValueError("Invalid Steam ID")
        
        url = f'{self.base_url}/ISteamUser/GetPlayerSummaries/v0002/'
        params = {'key': self.api_key, 'steamids': user}
        
        response = await client.get(url, params=params)
        handle_api_error(response)
        data = parse_json(response)
        player = data.get('response', {}).get('players', [{}])[0]
        return {
            'avatar': player.get('avatarfull'),
            'profileurl': format_steam_url(user),
            'personaname': player.get('personaname')
        }

    async def get_level(self, user):
        if not validate_steam_id(user):
            raise ValueError("Invalid Steam ID")
        
        url = f'{self.base_url}/IPlayerService/GetBadges/v1/'
        params = {'key': self.api_key, 'steamid': user}
        
        response = await client.get(url, params=params)
        handle_api_error(response)
        data = parse_json(response)
        return data.get('response', {}).get('player_level')

    async def get_badges(self, user):
        if not validate_steam_id(user):
            raise ValueError("Invalid Steam ID")
        
        url = f'{self.base_url}/IPlayerService/GetBadges/v1/'
        params = {'key': self.api_key, 'steamid': user}
        
        response = await client.get(url, params=params)
        handle_api_error(response)
        data = parse_json(response)
        return len(data.get('response', {}).get('badges', []))

    async def get_country(self, user):
        if not validate_steam_id(user):
            raise ValueError("Invalid Steam ID")
        
        url = f'{self.base_url}/ISteamUser/GetPlayerSummaries/v0002/'
        params = {'key': self.api_key, 'steamids': user}
        
        response = await client.get(url, params=params)
        handle_api_error(response)
        data = parse_json(response)
        player = data.get('response', {}).get('players', [{}])[0]
        country_code = player.get('loccountrycode', '')
        return country_code_to_flag(country_code) if country_code else 'No flag/bandera'

    async def close_client(self):
        await client.aclose()
