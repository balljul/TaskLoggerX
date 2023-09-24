mport mysql.connector
from tlx_cnf import db_cnf, Color
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

	def submit_worktime(self, start, stop, description, task):
		insert_statement = (
		"INSERT INTO worktime (starttime, endtime, description)"
		"VALUES (%s, %s, %s)"
		)
		insert_statement_task = (
		"INSERT INTO worktime_task (worktime_id, task_id)"
		"VALUES (%s, %s)"
		)
		get_task_id_statement = (
		"SELECT id FROM task WHERE name = %s"
		)

		# worktime table
		starttime = datetime.now().replace(hour = start, minute = 0, second = 0)
		endtime = datetime.now().replace(hour = stop, minute = 0, second = 0)
		data=(starttime, endtime, description)
		self.cursor.execute(insert_statement, data)
		self.conn.commit()
		worktime_id = self.cursor.lastrowid

		# worktime_task table
		self.cursor.execute(get_task_id_statement, (task,))
		task_id = self.cursor.fetchone()

		self.cursor.execute(insert_statement_task, (worktime_id, task_id[0]))
		self.conn.commit()
		print("Succesfully saved worktime")

	def create_task(self, name, description):
		insert_statement = (
		"INSERT INTO task (name, description)"
		"VALUES (%s, %s)"
		)

		data = (name, description)
		self.cursor.execute(insert_statement, data)
		self.conn.commit()
		print("Succesfully created task")

	def check_task_input(self, input):
		query = (
		"SELECT * FROM task"
		)
		data = self.cursor.execute(query)

		print(data)


	def list_task(self):
		query = (
		"SELECT * FROM task"
		)
		self.cursor.execute(query)

		for i in self.cursor:
			if i[2] != None:
				print(f"{Color.RED}ID: {Color.RESET}{i[0]}  {Color.GREEN}Name: {Color.RESET}{i[1]}  {Color.YELLOW}Description: {Color.RESET}{i[2]} " + "\n")
			else:
				print(f"{Color.RED}ID: {Color.RESET}{i[0]}  {Color.GREEN}Name: {Color.RESET}{i[1]}" + "\n")

