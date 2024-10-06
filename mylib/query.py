import sqlite3

def query(database="avengers.db", table="Avengers"):
    """Query the database for the top 5 rows of the specified table"""
    
    # Connect to the SQLite database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Execute the query to get the top 5 rows from the Avengers table
    cursor.execute(f"SELECT * FROM {table} LIMIT 5")
    
    # Fetch the results
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    return results
