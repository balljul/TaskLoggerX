import argparse
from time import localtime, gmtime, strftime
import mysql.connector

# General Information
parser = argparse.ArgumentParser(prog='TaskLoggerX', description='A dockerized Phyton CLI Tool to track and manage your tasks')

# Arguments
parser.add_argument('tlx')
parser.add_argument('-s', '--start', dest='start', action='store')
parser.add_argument('-e', '--end', dest='stop', action='store')
parser.add_argument('-ct', '--current-time', action='store_true', dest='show_time', help='Gives you the current CET and UTC Timestamp')

parser.add_argument('-dbs', '--database-show', action='store_true', dest='dbshow',  help='Shows all tables in the database')
parser.add_argument('--database-migrate', action='store_true', dest='dbmigrate', help='Migrates the database')
parser.add_argument('--database-delete', action='store_true', dest='dbdelete', help='A quick way to drop all tables in the database')

args = parser.parse_args()

# DB Logic
tlxdb = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'tlx_user',
	password = 'tlx123',
	database = 'tasklogger_db'
)

tlx_cursor = tlxdb.cursor()

if args.dbshow:
	tlx_cursor.execute("SHOW TABLES;")

	for x in tlx_cursor:
		print(x)

if args.dbmigrate:
	confirmation = input("Valuable Data could be lost. Are you sure? (Y/N): ")

	if confirmation == "Y":
		tlx_cursor.execute("DROP TABLE IF EXISTS worktime")
		print("Worktime Table dropped")
		tlx_cursor.execute("CREATE TABLE worktime (ID INT AUTO_INCREMENT PRIMARY KEY, starttime VARCHAR(255), endtime VARCHAR(255))")
		print("Freshly migrated")

	elif confirmation == "N":
		print("Database Migration cancelled")

	else:
		print("Please enter N(no) or Y(yes)")


if args.dbdelete:
	confirmation = input("Valuable Data could be lost. Are you sure? (Y/N): ")

	if confirmation == "Y":
		tlx_cursor.execute("DROP TABLE worktime")
		print("All Tables have been dropped")

	elif confirmation == "N":
		print("Database Deletion cancelled")

	else:
		print("Please enter N(no) or Y(yes)")


# Logic

class Color:
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RESET = '\033[0m'



if args.show_time:
	current_cet_timestamp = strftime("%a, %d %b %Y %H:%M:%S", localtime())
	current_utc_timestamp = strftime("%a, %d %b %Y %H:%M:%S", gmtime())

	print(f"{Color.GREEN}CET Timestamp:{Color.RESET} {current_cet_timestamp}")
	print(f"{Color.YELLOW}UTC Timestamp:{Color.RESET} {current_utc_timestamp}")

if args.start != None and args.stop != None:
	insert_statement = (
	"INSERT INTO worktime (starttime, endtime)"
	" VALUES (%s, %s)"
	)
	data = (args.start, args.stop)
	print(args.start)
	print(args.stop)

	tlx_cursor.execute(insert_statement, data)
	tlxdb.commit()
	print("Worktime saved")

elif args.start != None:
	print(args.start)
	print('Didn´t enter an end value')

elif args.stop != None:
	print(args.stop)
	print("Didnt enter a start value")
