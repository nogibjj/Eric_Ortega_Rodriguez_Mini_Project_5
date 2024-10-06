import sqlite3

def extract(database="avengers.db", table="Avengers"):
    """Extract data directly from the specified SQLite database and table"""
    
    # Connect to the SQLite database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    # Query to select all rows from the table (or a specific subset if needed)
    cursor.execute(f"SELECT * FROM {table}")
    
    # Fetch all rows from the table
    results = cursor.fetchall()
    
    # Close the connection
    conn.close()

    # Return the results (this could be data transformation, saving to a file, etc.)
    return results

if __name__ == "__main__":
    # Example of how to call the extract function and print the result
    data = extract(database="avengers.db", table="Avengers")
    for row in data:
        print(row)

