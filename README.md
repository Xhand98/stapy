

# `steam_api`

`steam_api` is a Python library for interacting with the Steam Web API. It provides easy-to-use asynchronous functions for retrieving various Steam user details, such as total playtime, Steam ID, owned games, profile picture, level, badges, and country flag.

## Features

- Retrieve total playtime for a user
- Resolve Steam vanity URLs to Steam IDs
- Get the number of owned games
- Fetch profile picture and profile URL
- Get player level and badges
- Retrieve country flag based on user location

## Installation

You can install `steam_api` using pip. If you want to use the latest development version, you can install it from the repository.

### Install from PyPI

```sh
pip install steam-api
```

### Install from Source

Clone the repository and install it in editable mode:

```sh
git clone https://github.com/Xhand98/steam-api.git
cd yourrepository
pip install -e .
```

## Usage

First, set up your environment with the Steam API key:

```sh
export STEAM_API_KEY='your_api_key_here'
```

### Example Usage

Here is a basic example of how to use the `steam_api` library:

```python
import asyncio
from steam_api import SteamAPI

async def main():
    api_key = "your_api_key_here"
    steam_api = SteamAPI(api_key)
  
    steam_id = "76561198006409530"  # Replace with actual Steam ID

    try:
        hours = await steam_api.get_hours(steam_id)
        print(f"Total hours played: {hours}")

        steam_id_resolved = await steam_api.get_steamid("vanity_url_here")
        print(f"Resolved Steam ID: {steam_id_resolved}")

        games_count = await steam_api.get_games(steam_id)
        print(f"Number of owned games: {games_count}")

        pic_info = await steam_api.get_pic(steam_id)
        print(f"Profile picture URL: {pic_info['avatar']}")
        print(f"Profile URL: {pic_info['profileurl']}")
        print(f"Persona name: {pic_info['personaname']}")

        level = await steam_api.get_level(steam_id)
        print(f"Player level: {level}")

        badges_count = await steam_api.get_badges(steam_id)
        print(f"Number of badges: {badges_count}")

        country_flag = await steam_api.get_country(steam_id)
        print(f"Country flag: {country_flag}")

    finally:
        await steam_api.close_client()

# Run the async main function
asyncio.run(main())
```

## Documentation

For detailed information on available functions and their parameters, refer to the source code or the [docs](https://github.com/Xhand98/yourrepository/wiki).

## Contributing

If you want to contribute to `steam_api`, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/Xhand98/yourrepository/issues) or contact [hendrickherrera9@.com](mailto:hendrickherrera9@.com).

---

Feel free to modify this template to fit your specific needs and preferences. The goal is to provide clear instructions and examples to help users get started with your library quickly.
