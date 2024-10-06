import sqlite3

def create_entry(database, table, entry_data):
    """Create a new entry in the table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    # Assuming entry_data is a tuple with values corresponding to the table columns
    cursor.execute(f"""
    INSERT INTO {table} (URL, Name_Alias, Appearances, Current, Gender, Probationary_Introl, 
    Full_Reserve_Avengers_Intro, Year, Years_since_joining, Honorary, Death1, Return1, Death2, 
    Return2, Death3, Return3, Death4, Return4, Death5, Notes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, entry_data)
    
    conn.commit()
    conn.close()


def read_entries(database, table):
    """Read all entries from the table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table}")
    results = cursor.fetchall()

    conn.close()
    return results


def update_entry(database, table, column, new_value, condition_column, condition_value):
    """Update an entry in the table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"""
    UPDATE {table}
    SET {column} = ?
    WHERE {condition_column} = ?
    """, (new_value, condition_value))
    
    conn.commit()
    conn.close()


def delete_entry(database, table, condition_column, condition_value):
    """Delete an entry from the table"""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {table} WHERE {condition_column} = ?", (condition_value,))
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Example usage of the CRUD functions
    db_name = "avengers.db"
    table_name = "Avengers"
    
    # Create
    new_entry = (
        'http://example.com', 'New Avenger', 10, 'YES', 'MALE', 'Intro1', 'Full', 2023, 
        1, 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'No notes'
    )
    create_entry(db_name, table_name, new_entry)
    
    # Read
    print("All entries:")
    entries = read_entries(db_name, table_name)
    for entry in entries:
        print(entry)
    
    # Update
    update_entry(db_name, table_name, 'Appearances', 15, 'Name_Alias', 'New Avenger')
    
    # Delete
    delete_entry(db_name, table_name, 'Name_Alias', 'New Avenger')
