# Migrations for TaskLoggerX

db_migration = """
CREATE DATABASE IF NOT EXISTS tasklogger_db;
"""

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
