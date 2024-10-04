import sqlite3

def query(database="new_database.db", table="new_table"):
    """Query the database for the top 5 rows of the specified table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} LIMIT 5")
    print(f"Top 5 rows of the {table} table:")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return "Success"
