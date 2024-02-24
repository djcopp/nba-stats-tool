from typing import Dict, Any
import requests
import os
import pandas as pd
import sqlite3


class RapidApiNBA:
    """
    Base class for interacting with the NBA API on RapidAPI.
    """

    def __init__(self):
        self.base_url = "https://api-nba-v1.p.rapidapi.com"
        self.headers = {
            "X-RapidAPI-Key": os.environ.get('NBA_API_KEY'),
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

    def _make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make a request to the NBA API.

        Parameters:
        - endpoint (str): The API endpoint to call.
        - params (Dict[str, Any], optional): The query parameters for the API call.

        Returns:
        - Dict[str, Any]: The JSON response from the API.
        """
        full_url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(full_url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()['response']
        except requests.RequestException as e:
            return {"error": str(e)}

    def _get_from_db(self, conn: sqlite3.Connection, table: str, season: str) -> pd.DataFrame:
        """
        Get data from the database for the specified table and season.

        Parameters:
        - conn (sqlite3.Connection): The connection to the SQLite database.
        - table (str): The table name to query.
        - season (str): The season to query data for.

        Returns:
        - pd.DataFrame: The data as a pandas DataFrame.
        """
        query = f"SELECT * FROM {table} WHERE season = ?"
        return pd.read_sql_query(query, conn, params=(season,))

    def _store_in_db(self, df: pd.DataFrame, conn: sqlite3.Connection, table: str) -> None:
        """
        Store the DataFrame into the specified SQLite database table.

        Parameters:
        - df (pd.DataFrame): The DataFrame to store.
        - conn (sqlite3.Connection): The connection to the SQLite database.
        - table (str): The table name where data will be stored.
        """
        df.to_sql(table, conn, if_exists='append', index=False)


class Standings(RapidApiNBA):
    
    def get_standings(self, season: str, conn: sqlite3.Connection) -> pd.DataFrame:
        """
        Retrieves or stores the NBA standings for a specific season.

        Parameters:
        - season (str): The NBA season for which you want the standings.
        - conn (sqlite3.Connection): The connection to the SQLite database.

        Returns:
        - pd.DataFrame: The standings for the specified season.
        """
        table = 'standings'
        df = self._get_from_db(conn, table, season)
        if not df.empty:
            return df

        data = self._make_request("/standings", params={"league": "standard", "season": season})
        if 'error' not in data:
            df = pd.DataFrame([
                {f"team_{k}": v for k, v in standing['team'].items()}|{f"conference_{k}": v for k, v in standing['conference'].items()}
                for standing in data
            ])
            df['season'] = season
            self._store_in_db(df, conn, table)
            return df
        else:
            return pd.DataFrame(data)
        
class PlayersByTeamSeason(RapidApiNBA):
    """
    Retrieves players for a specific team in a given season.
    """
    
    def get_players_by_team_season(self, team_id: str, season: str) -> Dict[str, Any]:
        endpoint = "/players"
        querystring = {"team": team_id, "season": season}
        
        data = self._make_request(endpoint, querystring)

        if 'error' not in data:
            return data
    
class PlayerStatistics(RapidApiNBA):
    """
    Retrieves a player's statistics for all games in the specified season.
    """
    
    def get_player_statistics(self, player_id: str, season: str) -> Dict[str, Any]:
        endpoint = "/players/statistics"
        querystring = {"id": player_id, "season": season}
        data = self._make_request(endpoint, querystring)

        return None
