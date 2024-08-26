import requests
import sqlite3
from datetime import datetime

def fetch_queue_time(api_url, park_id):
    response = requests.get(f'{api_url}/{park_id}/queue_times.json')
    if response.status_code == 200:
        return response.json()
    return None

def update_queue_time(api_url):
    conn = sqlite3.connect('data/database.sqlite')
    cursor = conn.cursor()

    cursor.execute('SELECT park_id FROM theme_parks')
    parks = cursor.fetchall()

    for park_id_tuple in parks:
        park_id = park_id_tuple[0]
        queue_data = fetch_queue_time(api_url, park_id)

        if queue_data:
            timestamp = datetime.now()

            for ride, wait_time in queue_data['wait_times'].items():
                cursor.execute('''
                    INSERT INTO queue_times(park_id, timestamp, ride_name, wait_time)
                    VALUES(?, ?, ?, ?)
                    ''', (park_id, timestamp, ride, wait_time))
                
    conn.commit()
    conn.close()

if __name__ == '__main__':
    api_url = 'https://queue-times.com/parks'
    update_queue_time(api_url)