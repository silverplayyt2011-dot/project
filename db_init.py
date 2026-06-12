import sqlite3
sqlite_connection = sqlite3.connect('primer.db')

cursor = sqlite_connection.cursor()

query = """CREATE TABLE IF NOT EXISTS users (
			user_id ID TEXT NOT NULL);"""

cursor.execute(query)

query = """CREATE TABLE IF NOT EXISTS zadachi (
			zadacha_id INTEGER PRIMARY KEY AUTOINCREMENT,
			user_id TEXT,
			zadacha TEXT,
			zadacha_set DATE DEFAULT CURRENT_DATE,
			zadacha_done DATE,
			status INTEGER NOT NULL DEFAULT 0);"""

cursor.execute(query)
sqlite_connection.commit()
sqlite_connection.close()