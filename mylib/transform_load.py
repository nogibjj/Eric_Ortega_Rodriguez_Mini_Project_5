import sqlite3
import csv
import os

# Load the CSV file and insert it into a new SQLite3 database
def load(dataset="data/avengers.csv", db_name="avengers.db", table_name="Avengers"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Prints the full working directory and path
    print(os.getcwd())
    
    # Open the CSV file with the correct encoding
    with open(dataset, newline='', encoding="ISO-8859-1") as csvfile:
        payload = csv.reader(csvfile, delimiter=',')
        
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        
        # Drop the table if it already exists, then create a new one
        c.execute(f"DROP TABLE IF EXISTS {table_name}")
        c.execute(f"""
        CREATE TABLE {table_name} (
            Appearances INTEGER, 
            Current TEXT, 
            Gender TEXT, 
            Year INTEGER
        )
        """)
        
        # Skip the header and insert the data into the table
        next(payload)  # Skip header row
        c.executemany(f"INSERT INTO {table_name} VALUES (?,?,?,?,?)", payload)
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        
    return db_name


if __name__== "__main__":
    load()
