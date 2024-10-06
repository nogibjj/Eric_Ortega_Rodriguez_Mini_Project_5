import os
import requests

def extract(url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/avengers/avengers.csv",
            file_path="data/avengers.csv"):
    """Extract a dataset from the provided URL to a specified file path"""
    
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Download the file from the URL and save it to the file path
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)

if __name__== "__main__":
    extract()

