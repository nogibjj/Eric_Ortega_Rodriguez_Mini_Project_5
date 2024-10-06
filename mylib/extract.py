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
def test_extract_empty_table():
    """Test extracting data from an empty table."""
    db_name = "empty_avengers.db"
    table_name = "Avengers"
    
    # Ensure the database and table are created but no data is loaded
    load(dataset=None, db_name=db_name, table_name=table_name)  # You can skip loading any data
    
    # Extract data from the empty table
    data = extract(database=db_name, table=table_name)
    
    # Verify that the data is empty
    assert len(data) == 0  # Expect no rows in an empty table


if __name__ == "__main__":
    # Example of how to call the extract function and print the result
    data = extract(database="avengers.db", table="Avengers")
    for row in data:
        print(row)

