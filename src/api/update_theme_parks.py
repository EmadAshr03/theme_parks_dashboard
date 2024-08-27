import requests
import pandas as pd
import sqlite3
from datetime import datetime

def fetch_theme_park_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
def update_theme_parks(api_url):
    parks_data = fetch_theme_park_data(api_url)
    if parks_data:
        conn = sqlite3.connect('data/database.sqlite')
        cursor = conn.cursor()

        for company in parks_data:
            for park in company['parks']:
                park_id = park['id']
                park_name = park['name']
                last_updated = datetime.now()

            cursor.execute('''
                INSERT INTO theme_parks (park_id, park_name, last_updated)
                VALUES (?, ?, ?)
                ON CONFLICT(park_id)) DO UPDATE SET
                    park_name=excluded.park_name,
                    last_updated=excluded.last_updated
            ''', (park_id, park_name, last_updated))

        conn.commit()
        conn.close()

if __name__ == '__main__':
    url = 'https://queue-times.com/parks.json'
    update_theme_parks(url)
