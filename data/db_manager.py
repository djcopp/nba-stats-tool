# db_manager.py
import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """Create a table with the create_table_sql statement."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

# Example usage
database = "nba_stats.db"

sql_create_players_table = """CREATE TABLE IF NOT EXISTS players (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    stats text
                                );"""

# Create a database connection
conn = create_connection(database)

# Create table
if conn is not None:
    create_table(conn, sql_create_players_table)
else:
    print("Error! Cannot create the database connection.")
