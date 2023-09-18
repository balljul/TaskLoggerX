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
    
def drop_worktime_table():
    tlx_cursor.execute("DROP TABLE worktime")
    print("Worktime Table dropped")  
    
def migrate_database():
    tlx_cursor.execute("DROP TABLE IF EXISTS worktime")
    print("Worktime Table dropped")
    tlx_cursor.execute("CREATE TABLE worktime (ID INT AUTO_INCREMENT PRIMARY KEY, starttime VARCHAR(255), endtime VARCHAR(255))")
    print("Freshly migrated")


def submit_worktime(starttime, endtime):
    insert_statement = (
	"INSERT INTO worktime (starttime, endtime)"
	"VALUES (%s, %s)"
	)
    data=(starttime, endtime)
    tlx_cursor.execute(insert_statement, data)
    tlxdb.commit()
    print("Succesfully saved worktime")