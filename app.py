from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_latest_reading():
    conn = sqlite3.connect('weather.db')
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    return row

def get_historical_readings():
    conn = sqlite3.connect('weather.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    # Grab last 24 entries for the timeline visualization
    cursor.execute('SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 24')
    rows = cursor.fetchall()
    conn.close()
    return list(reversed(rows)) # Reverse so chronological order goes left-to-right

@app.route('/')
def index():
    latest = get_latest_reading()
    history = get_historical_readings()
    return render_template('index.html', latest=latest, history=history)

if __name__ == '__main__':
    # host='0.0.0.0' allows you to connect from any device on your Wi-Fi network
    app.run(host='0.0.0.0', port=5000, debug=True)

