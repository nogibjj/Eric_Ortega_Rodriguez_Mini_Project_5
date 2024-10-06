import sqlite3
import csv
import os

# Load the CSV file and insert it into a new SQLite3 database
def load(dataset="data/avengers.csv", db_name="avengers.db", table_name="Avengers"):
    """Transforms and Loads data into the local SQLite3 database"""
    
    print("Current directory:", os.getcwd())

    try:
        # Open the CSV file
        with open(dataset, newline='', encoding="ISO-8859-1") as csvfile:
            payload = csv.reader(csvfile, delimiter=',')
            
            # Connect to the SQLite database (or create it if it doesn't exist)
            conn = sqlite3.connect(db_name)
            c = conn.cursor()
            
            # Drop the table if it already exists, then create a new one
            c.execute(f"DROP TABLE IF EXISTS {table_name}")
            c.execute(f"""
            CREATE TABLE {table_name} (
                URL TEXT,
                Name_Alias TEXT,
                Appearances INTEGER, 
                Current TEXT, 
                Gender TEXT,
                Probationary_Introl TEXT,
                Full_Reserve_Avengers_Intro TEXT,
                Year INTEGER,
                Years_since_joining INTEGER,
                Honorary TEXT,
                Death1 TEXT,
                Return1 TEXT,
                Death2 TEXT,
                Return2 TEXT,
                Death3 TEXT,
                Return3 TEXT,
                Death4 TEXT,
                Return4 TEXT,
                Death5 TEXT,
                Return5 TEXT,
                Notes TEXT
            )
            """)
            
            # Skip the header
            next(payload)

            # Prepare and sanitize data before inserting
            sanitized_payload = [
                tuple(map(lambda x: x.strip() if isinstance(x, str) else x, row)) for row in payload
            ]

            # Insert all rows into the table
            c.executemany(
                f"INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                sanitized_payload
            )
            
            # Commit the changes and close the connection
            conn.commit()
            print(f"Data loaded successfully into {table_name} table.")
            
        conn.close()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return db_name

if __name__ == "__main__":
    load()
