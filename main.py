from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

# Paths and parameters for the new dataset
dataset_url = "https://github.com/fivethirtyeight/data/raw/refs/heads/master/avengers/avengers.csv"
dataset_path = "data/avengers.csv"
db_name = "avengers.db"
table_name = "Avengers"

# Extract
print("Extracting data...")
extract(url=dataset_url, file_path=dataset_path)

# Transform and load
print("Transforming and loading data...")
load(dataset=dataset_path, db_name=db_name, table_name=table_name)

# Query
print("Querying data...")
query(database=db_name, table=table_name)
