import sqlite3
import csv

def load(dataset="data/avengers.csv", db_name="avengers.db", table_name="Avengers"):
    """Load data from a CSV file into an SQLite database"""
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the table if it doesn't exist (with 20 columns)
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
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
        Notes TEXT
    )
    """)

    # Load data from CSV file
    with open(dataset, newline='', encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            # Adjust the INSERT statement to insert only 20 values, matching the table
            cursor.execute(
                f"""
                INSERT INTO {table_name} (URL, Name_Alias, Appearances, Current, Gender, Probationary_Introl, 
                Full_Reserve_Avengers_Intro, Year, Years_since_joining, Honorary, Death1, Return1, Death2, 
                Return2, Death3, Return3, Death4, Return4, Death5, Notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                row[:20]
            )

    # Commit changes and close connection
    conn.commit()
    conn.close()

def transform(data):
    """Example transform function - you can apply specific transformations here"""
    return data

if __name__ == "__main__":
    # Example of loading and transforming the data
    load(dataset="data/avengers.csv", db_name="avengers.db", table_name="Avengers")

    # Assuming you extracted the data using your extract function
    from extract import extract
    data = extract(database="avengers.db", table="Avengers")
    
    # Apply transformation if necessary
    transformed_data = transform(data)

    # Print the transformed data
    for row in transformed_data:
        print(row)
