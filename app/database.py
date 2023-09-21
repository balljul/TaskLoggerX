import mysql.connector
from tlx_cnf import db_cnf

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

	def submit_worktime(starttime, endtime, description):
	    insert_statement = (
		"INSERT INTO worktime (starttime, endtime, description)"
		"VALUES (%s, %s, %s)"
		)
	    data=(starttime, endtime, description)
	    tlx_cursor.execute(insert_statement, data)
	    tlxdb.commit()
	    print("Succesfully saved worktime")

