from data.api_wrapper import get_available_seasons, Standings
from data.db_manager import create_connection, create_table

import sqlite3
import pandas as pd

def main():
    
    conn = sqlite3.connect('nba_data.db')
    standings_instance = Standings()
    standings_df = standings_instance.get_standings("2022", conn)
    print(standings_df)

if __name__ == "__main__":
    main()
