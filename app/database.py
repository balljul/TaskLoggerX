import mysql.connector
from tlx_cnf import db_cnf
from datetime import datetime, timedelta

class taskLoggerDb:
	def __init__(self, host = db_cnf.HOST, user = db_cnf.USER, password = db_cnf.PASSWORD, database = db_cnf.DATABASE):
		self.conn = mysql.connector.connect(
			host = host,
			user = user,
			password = password,
			database = database
		)
		self.cursor = self.conn.cursor()

	def show_tables(self):
	    self.cursor.execute("SHOW TABLES;")
	    for x in self.cursor:
	        print(x)

	def submit_worktime(self, start, stop, description):
		insert_statement = (
		"INSERT INTO worktime (starttime, endtime, description)"
		"VALUES (%s, %s, %s)"
		)

		starttime = datetime.now().replace(hour = start, minute = 0, second = 0)
		endtime = datetime.now().replace(hour = stop, minute = 0, second = 0)

		data=(starttime, endtime, description)
		self.cursor.execute(insert_statement, data)
		self.conn.commit()
		print("Succesfully saved worktime")

	def create_task(self):
		print("This function creates Tasks")
