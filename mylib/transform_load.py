import sqlite3
import csv
import os

# Load the CSV file and insert it into a new SQLite3 database
def load(dataset="/path/to/your/new_dataset.csv", db_name="new_database.db", table_name="new_table"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Prints the full working directory and path
    print(os.getcwd())
    
    # Open the CSV file
    with open(dataset, newline='') as csvfile:
        payload = csv.reader(csvfile, delimiter=',')
        
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        
        # Drop the table if it already exists, then create a new one
        c.execute(f"DROP TABLE IF EXISTS {table_name}")
        c.execute(f"""
        CREATE TABLE {table_name} (
            id INTEGER PRIMARY KEY,
            general_name TEXT, 
            count_products INTEGER, 
            ingred_FPro REAL, 
            avg_FPro_products REAL, 
            avg_distance_root REAL, 
            ingred_normalization_term REAL, 
            semantic_tree_name TEXT, 
            semantic_tree_node TEXT)
        """)
        
        # Skip the header and insert the data into the table
        next(payload)  # Skip header row
        c.executemany(f"INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?,?,?)", payload)
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        
    return db_name
