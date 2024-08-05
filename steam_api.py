import httpx
import os

# Create a single AsyncClient instance
client = httpx.AsyncClient()

async def fetch_data(url, params=None):
    response = await client.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

class SteamAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.steampowered.com"

    async def get_hours(self, user):
        url = f'{self.base_url}/IPlayerService/GetOwnedGames/v1/'
        params = {'key': self.api_key, 'steamid': user, 'include_appinfo': 1, 'include_played_free_games': 1}
        
        data = await fetch_data(url, params=params)
        total_hours = sum(game.get('playtime_forever', 0) / 60 for game in data.get('response', {}).get('games', []))
        return total_hours

    async def get_steamid(self, user):
        url = f'{self.base_url}/ISteamUser/ResolveVanityURL/v0001/'
        params = {'key': self.api_key, 'vanityurl': user}
        
        data = await fetch_data(url, params=params)
        return data.get('response', {}).get('steamid')

    async def get_games(self, user):
        url = f'{self.base_url}/IPlayerService/GetOwnedGames/v1/'
        params = {'key': self.api_key, 'steamid': user, 'include_appinfo': 1}
        
        data = await fetch_data(url, params=params)
        return len(data.get('response', {}).get('games', []))

    async def get_pic(self, user):
        url = f'{self.base_url}/ISteamUser/GetPlayerSummaries/v0002/'
        params = {'key': self.api_key, 'steamids': user}
        
        data = await fetch_data(url, params=params)
        player = data.get('response', {}).get('players', [{}])[0]
        return {
            'avatar': player.get('avatarfull'),
            'profileurl': player.get('profileurl'),
            'personaname': player.get('personaname')
        }

    async def get_level(self, user):
        url = f'{self.base_url}/IPlayerService/GetBadges/v1/'
        params = {'key': self.api_key, 'steamid': user}
        
        data = await fetch_data(url, params=params)
        return data.get('response', {}).get('player_level')

    async def get_badges(self, user):
        url = f'{self.base_url}/IPlayerService/GetBadges/v1/'
        params = {'key': self.api_key, 'steamid': user}
        
        data = await fetch_data(url, params=params)
        return len(data.get('response', {}).get('badges', []))

    async def get_country(self, user):
        url = f'{self.base_url}/ISteamUser/GetPlayerSummaries/v0002/'
        params = {'key': self.api_key, 'steamids': user}
        
        data = await fetch_data(url, params=params)
        player = data.get('response', {}).get('players', [{}])[0]
        country_code = player.get('loccountrycode', '')

        def country_code_to_flag(country_code):
            country_code = country_code.upper()
            return ''.join(chr(0x1F1E6 + ord(char) - ord('A')) for char in country_code)

        return country_code_to_flag(country_code) if country_code else 'No flag/bandera'

    async def close_client(self):
        await client.aclose()
