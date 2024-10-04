import requests

def extract(url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/avengers/avengers.csv", 
            file_path="data/avengers.csv"):
    """Extract a dataset from the provided URL to a specified file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path


