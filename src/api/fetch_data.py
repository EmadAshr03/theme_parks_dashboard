import requests
import pandas as pd

def fetch_theme_park_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

url = 'https://queue-times.com/parks.json'
fetch_theme_park_data(url)