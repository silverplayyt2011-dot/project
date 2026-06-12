import sqlite3

class Database:
	def __init__(self):
		self.sqlite_connection = sqlite3.connect('primer.db')
		self.cursor = self.sqlite_connection.cursor()

	def add_user(self, user_id):
		query = "INSERT INTO users (user_id) VALUES (?)"
		self.cursor.execute(query, (user_id,))
		self.sqlite_connection.commit()

	def add_task(self, user_id, task):
		query = "INSERT INTO zadachi (user_id, zadacha) VALUES (?, ?)"
		self.cursor.execute(query, (user_id, task))
		self.sqlite_connection.commit()

	def get_zadachi_by_ip(self, user_id):
		query = "SELECT zadacha, zadacha_set, zadacha_done, status, zadacha_id FROM zadachi WHERE user_id = ?"
		self.cursor.execute(query, (user_id,))
		result = self.cursor.fetchall()
		return result

	def delete_zadacha_by_id(self, zadacha_id):
		query = "DELETE FROM zadachi WHERE zadacha_id = ?"
		self.cursor.execute(query, (zadacha_id,))
		self.sqlite_connection.commit()

	def change_zadacha_done(self, zadacha_id):
		query = "UPDATE zadachi SET status = ?, zadacha_done = CURRENT_DATE  WHERE zadacha_id = ?"
		self.cursor.execute(query, (1, zadacha_id))
		self.sqlite_connection.commit()

	def close(self):
		self.sqlite_connection.close()
