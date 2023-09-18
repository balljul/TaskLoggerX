import arguments
import database
import tlx_clock

# DB Logic

if arguments.args.dbshow:
	database.show_tables()
 
if arguments.args.dbmigrate:
	confirmation = input("Valuable Data could be lost. Are you sure? (Y/N): ")

	if confirmation == "Y":
		database.migrate_database()
	elif confirmation == "N":
		print("Migration cancelled")
	else:
		print("Please enter N(no) or Y(yes)")

if arguments.args.dbdelete:
	confirmation = input("Valuable Data could be lost. Are you sure? (Y/N): ")

	if confirmation == "Y":
		database.drop_worktime_table()
	elif confirmation == "N":
		print("Database Deletion cancelled")
	else:
		print("Please enter N(no) or Y(yes)")





if arguments.args.show_time:
	tlx_clock.output_ct_timestamps()

if arguments.args.start != None and arguments.args.stop != None:
	database.submit_worktime(arguments.args.start, arguments.args.stop)
elif arguments.args.start != None:
	print(arguments.args.start)
	print('Didn´t enter an end value')
elif arguments.args.stop != None:
	print(arguments.args.stop)
	print("Didnt enter a start value")
