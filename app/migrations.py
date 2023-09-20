import mysql.connector
from tlx_cnf import db_cnf
# Migrations for TaskLoggerX
class taskLoggerMigrations:
	def __inti__(self, host, user, password, database):
		self.conn = mysql.connector.connect(
			host=host,
			user=user,
			password=password,
			database=database
		)
		self.cusor = slef.conn.cursor()
	def test:
		print(db_cnf.host())
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
		CREATE TABLE IF NOT EXISTS status_worktime
			FOREIGN KEY (status_id) REFERENCES status(id)
			FOREIGN KEY (worktime_id) REFERENCES worktime(id)
		)
		"""


		worktime_task_table = """
		CREATE TABLE IF NOT EXISTS worktime_task
			FOREIGN KEY (worktime_id) REFERENCES worktime(id)
			FOREIGN KEY (task_id) REFERENCES task(id)
		)
		"""


		status_task_table = """
		CREATE TABLE IF NOT EXISTS status_task (
			FOREIGN KEY (status_id) REFERENCES status(id)
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


