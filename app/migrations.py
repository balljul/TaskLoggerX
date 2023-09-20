import mysql.connector
from tlx_cnf import db_cnf
# Migrations for TaskLoggerX
class taskLoggerMigrations:
	def __init__(self, host = db_cnf.HOST, user = db_cnf.USER, password = db_cnf.PASSWORD, database = db_cnf.DATABASE):
		self.conn = mysql.connector.connect(
			host=host,
			user=user,
			password=password,
			database=database
		)
		self.cursor = self.conn.cursor()
	def drop_shema(self):
		drop_tables = """
		DROP TABLE IF EXISTS worktime, task, status, worktime_task, status_task, status_worktime;
		"""
		self.cursor.execute(drop_tables)
	def create_tables(self):
		table_worktime = """
		CREATE TABLE IF NOT EXISTS worktime (
			id INT AUTO_INCREMENT PRIMARY KEY,
			starttime DATETIME NOT NULL,
			endtime DATETIME NOT NULL,
			description VARCHAR(255) 
		)
		"""

		table_task = """
		CREATE TABLE IF NOT EXISTS task (
			id INT AUTO_INCREMENT PRIMARY KEY,
			name VARCHAR(255) NOT NULL,
			description VARCHAR(255)
		)
		"""

		table_status = """
		CREATE TABLE IF NOT EXISTS status (
			id INT AUTO_INCREMENT PRIMARY KEY,
			name VARCHAR(255) NOT NULL,
			description VARCHAR(255)
		)
		"""
		status_worktime_table = """
		CREATE TABLE IF NOT EXISTS status_worktime (
		    status_id INT,
		    worktime_id INT,
		    FOREIGN KEY (status_id) REFERENCES status(id),
		    FOREIGN KEY (worktime_id) REFERENCES worktime(id)
		)
		"""

		worktime_task_table = """
		CREATE TABLE IF NOT EXISTS worktime_task (
			worktime_id INT,
			task_id INT,
			FOREIGN KEY (worktime_id) REFERENCES worktime(id),
			FOREIGN KEY (task_id) REFERENCES task(id)
		)
		"""


		status_task_table = """
		CREATE TABLE IF NOT EXISTS status_task (
			status_id INT,
			task_id INT,
			FOREIGN KEY (status_id) REFERENCES status(id),
			FOREIGN KEY (task_id) REFERENCES task(id)
		)
		"""

		self.cursor.execute(table_worktime)
		self.cursor.execute(table_task)
		self.cursor.execute(table_status)
		self.cursor.execute(status_worktime_table)
		self.cursor.execute(worktime_task_table)
		self.cursor.execute(status_task_table)
		self.conn.commit()

	def close_connection(self):
		self.cursor.close()
		self.conn.close()


