import sqlite3

def init_db():
    # Connects to database file (creates it if it does not exist)
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    
    # Create table for structured historical storage
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temperature REAL,
            humidity REAL,
            pressure REAL,
            is_raining INTEGER
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")

