import mysql.connector

tlxdb = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'tlx_user',
	password = 'tlx123',
	database = 'tasklogger_db'
)

tlx_cursor = tlxdb.cursor()

def show_tables():
    tlx_cursor.execute("SHOW TABLES;")
    for x in tlx_cursor:
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
