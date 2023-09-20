import mysql.connector
from tlx_cnf import db_cnf

class taskLoggerSeeders:
	def __init__(self, host = db_cnf.HOST, user = db_cnf.USER, password = db_cnf.PASSWORD, database = db_cnf.DATABASE):
		self.conn = mysql.connector.connect(
			host = host,
			user = user,
			password = password,
			database = database
		)
		self.cursor = self.conn.cursor()

	def seed_tables(self):
		statuses = [["active", "Task/Worktime Entry is active"], ["descarded", "Task/Worktime Entry is descarded"], ["outdated", "Task/Worktime is outdated"]]
		status_seeder_query = "INSERT INTO status (name, description) VALUES (%s, %s)"

		for status in statuses:
			self.cursor.execute(status_seeder_query, (status[0], status[1]))
			self.conn.commit()

