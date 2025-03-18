# utils/database.py
import sqlite3
from config import DB_FILE

# Create table if not exists
def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pollination_data
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       feature1 REAL,
                       feature2 REAL,
                       pollination_success INTEGER)''')
    conn.commit()
    conn.close()

# Insert data into the database
def insert_data(feature1, feature2, pollination_success):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pollination_data (feature1, feature2, pollination_success) VALUES (?, ?, ?)",
                   (feature1, feature2, pollination_success))
    conn.commit()
    conn.close()

# Fetch all data
def get_all_data():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pollination_data")
    data = cursor.fetchall()
    conn.close()
    return data

# Initialize table
create_table()
