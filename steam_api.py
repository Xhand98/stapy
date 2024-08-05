import requests

class SteamAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.steampowered.com"
        
    def _make_requests(self, endpoint, params):
        url = f"{self.base_url}/{endpoint}"
        params['key'] = self.api_key
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
        return response.json() 
    
    def get_player_summaries(self, steam_ids):
        """
        Fetches player summary data for the given Steam IDs.
    
        :param steam_ids: A comma-separated string or list of Steam IDs
        :return: A dictionary containing player summary data
        """
        if isinstance(steam_ids, list):
            steam_ids = ",".join(steam_ids)

        params = {
            'steamids': steam_ids
        }
        return self._make_request('ISteamUser/GetPlayerSummaries/v2/', params)
