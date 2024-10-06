import os
import pytest
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

# Paths and parameters for the test
db_name = "test_avengers.db"
table_name = "Avengers"
dataset_path = "data/avengers.csv"

def test_extract():
    """Test the extraction of data from the database"""
    # Ensure the test database and table exist before extracting
    if not os.path.exists(db_name):
        load(dataset=dataset_path, db_name=db_name, table_name=table_name)

    # Extract data from the database
    data = extract(database=db_name, table=table_name)

    # Check if data was extracted and assert that it's not empty
    assert data is not None
    assert len(data) > 0  # Ensure some data was extracted

def test_query():
    """Test the query function"""
    # Ensure the database and table are created before running the query
    if not os.path.exists(db_name):
        load(dataset=dataset_path, db_name=db_name, table_name=table_name)

    # Now test the query function
    result = query(database=db_name, table=table_name)

    # Check if query result is valid
    assert result is not None
    assert len(result) == 5  # Check if it returns the top 5 rows

def test_load():
    """Test the loading of CSV data into the database"""
    # Clean up previous test database
    if os.path.exists(db_name):
        os.remove(db_name)
    
    # Load data from the CSV into the database
    load(dataset=dataset_path, db_name=db_name, table_name=table_name)
    
    # Check if database file was created
    assert os.path.exists(db_name)

    # Verify the data has been loaded by querying the table
    data = extract(database=db_name, table=table_name)
    assert len(data) > 0  # Ensure data was loaded

if __name__ == "__main__":
    pytest.main()
