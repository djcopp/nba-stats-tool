# main.py
from data.api_wrapper import get_available_seasons, get_standings
from data.db_manager import create_connection, create_table

def main():
    
    here = get_available_seasons()
    
    yeet = 0

if __name__ == "__main__":
    main()
