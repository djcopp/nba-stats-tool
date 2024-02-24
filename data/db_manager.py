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

def add_column_to_table(db_file: str, table_name: str, new_column_name: str, column_type: str):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    alter_table_sql = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {column_type};"

    cursor.execute(alter_table_sql)

    conn.commit()
    conn.close()