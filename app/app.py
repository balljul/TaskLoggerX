import arguments
import database
from migrations import taskLoggerMigrations
import tlx_clock

# DB Logic

migrations = taskLoggerMigrations()

if arguments.args.dbshow:
	database.show_tables()

if arguments.args.dbmigrate:
	confirmation = input("Valuable Data could be lost. Are you sure? (Y/n): ")

	if confirmation == "Y":
		migrations.create_tables()
	elif confirmation == "N":
		print("Migration cancelled")
	else:
		print("Please enter N(no) or Y(yes)")

if arguments.args.dbdrop:
	confirmation = input("Valuable Data could be lost. Are you sure? (Y/n): ")

	if confirmation == "Y":
		migrations.drop_shema()
		print("Shema was dropped")
	elif confirmation == "N":
		print("Database Deletion cancelled")
	else:
		print("Please enter N(no) or Y(yes)")





if arguments.args.show_time:
	tlx_clock.output_ct_timestamps()

if arguments.args.start != None and arguments.args.stop != None:
	if arguments.args.description != None:
		database.submit_worktime(arguments.args.start, arguments.args.stop, arguments.args.description)
	else:
		database.submit_worktime(arguments.args.start, arguments.args.stop, "")

elif arguments.args.start != None:
	print(arguments.args.start)
	print('Didn´t enter an end value')
elif arguments.args.stop != None:
	print(arguments.args.stop)
	print("Didnt enter a start value")
