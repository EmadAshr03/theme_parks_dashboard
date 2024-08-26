import sqlite3

def create_tables():
    conn = sqlite3.connect('data/database.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS theme_parks(
            park_id INTEGER PRIMARY KEY,
            park_name TEXT,
            last_updated TIMESTAMP
        )'''
    )

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queue_time(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        park_id INTEGER,
        timestamp TIMESTAMP,
        ride_name TEXT,
        wait_time INTEGER,
        FOREIGN KEY (park_id) REFERENCES theme_parks (park_id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    