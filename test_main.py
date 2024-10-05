"""
Test goes here

"""
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

def test_extract():
    # Example test for extraction function
    dataset_url = "https://github.com/fivethirtyeight/data/raw/refs/heads/master/avengers/avengers.csv"
    file_path = "data/test_avengers.csv"
    assert extract(url=dataset_url, file_path=file_path) == file_path

def test_load():
    # Example test for the load function
    dataset_path = "data/test_avengers.csv"
    db_name = "test_avengers.db"
    table_name = "Avengers"
    assert load(dataset=dataset_path, db_name=db_name, table_name=table_name) == db_name

def test_query():
    # Example test for the query function
    db_name = "test_avengers.db"
    table_name = "Avengers"
    result = query(database=db_name, table=table_name)
    assert result == "Success"
