import sqlite3

def query(database="new_database.db", table="new_table"):
    """Query the database for the top 5 rows of the specified table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    # Make sure the query limits the result to 5 rows
    cursor.execute(f"SELECT * FROM {table} LIMIT 5")
    
    result = cursor.fetchall()
    conn.close()
    return result

