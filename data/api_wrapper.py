from typing import Dict, Any
import requests
import os

def get_player_statistics(player_id: str, season: str) -> Dict[str, Any]:
    """
    Retrieves a player's statistics for all games in the specified season.

    Parameters:
    - player_id (str): The unique identifier for the player.
    - season (str): The NBA season for which you want data, in the format "YYYY".

    Returns:
    - Dict[str, Any]: A JSON response containing the player's statistics.
    """
    url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
    headers = {
        "X-RapidAPI-Key": os.environ.get('NBA_API_KEY'),
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    querystring = {"id": player_id, "season": season}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def get_available_seasons() -> Dict[str, Any]:
    """
    Retrieves the available NBA seasons from the API.

    Returns:
    - Dict[str, Any]: A JSON response containing the available seasons.
    """
    url = "https://api-nba-v1.p.rapidapi.com/seasons"
    headers = {
        "X-RapidAPI-Key": os.environ.get('NBA_API_KEY'),
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def get_standings(season: str) -> Dict[str, Any]:
    """
    Retrieves the NBA standings for a specific season.

    Parameters:
    - season (str): The NBA season for which you want the standings, in the format "YYYY".

    Returns:
    - Dict[str, Any]: A JSON response containing the standings for the specified season.
    """
    url = "https://api-nba-v1.p.rapidapi.com/standings"
    headers = {
        "X-RapidAPI-Key": os.environ.get('NBA_API_KEY'),
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    querystring = {"league": "standard", "season": season}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def get_players_by_team_season(team_id: str, season: str) -> Dict[str, Any]:
    """
    Retrieves players for a specific team in a given season.

    Parameters:
    - team_id (str): The unique identifier for the team.
    - season (str): The NBA season for which you want the players, in the format "YYYY".

    Returns:
    - Dict[str, Any]: A JSON response containing the players for the specified team and season.
    """
    url = "https://api-nba-v1.p.rapidapi.com/players"
    headers = {
        "X-RapidAPI-Key": os.environ.get('NBA_API_KEY'),
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    querystring = {"team": team_id, "season": season}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
