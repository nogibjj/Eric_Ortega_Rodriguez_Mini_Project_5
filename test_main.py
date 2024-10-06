import os
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

def test_extract():
    """Test the extraction of data"""
    # Ensure data directory and file are present
    if not os.path.exists('data/avengers.csv'):
        extract()

    # Check if the file was created
    assert os.path.exists('data/avengers.csv')

def test_query():
    """Test the query function"""
    db_name = "test_avengers.db"
    table_name = "Avengers"
    
    # Ensure the database and table are created before running the query
    if not os.path.exists(db_name):
        load(dataset="data/avengers.csv", db_name=db_name, table_name=table_name)

    # Now test the query function
    result = query(database=db_name, table=table_name)
    assert result is not None
    assert len(result) == 5
