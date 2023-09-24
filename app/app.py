#! /usr/bin/env python3
import arguments
from database import taskLoggerDb
from migrations import taskLoggerMigrations
from seeder import taskLoggerSeeders
import tlx_clock

# DB Logic

migrations = taskLoggerMigrations()
seeders = taskLoggerSeeders()
database = taskLoggerDb()

# dlx Module
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

if arguments.args.dbseed:
	seeders.seed_tables()
	seeders.seed_tasks()
	print("Database succesfully seeded")


# Clock Module

if arguments.args.show_time:
	tlx_clock.output_ct_timestamps()


# wlx Module

if arguments.args.start != None and arguments.args.stop != None:
	description = arguments.args.description if arguments.args.description != None else ""
	task = arguments.args.append if arguments.args.append != None else ""

	database.submit_worktime(arguments.args.start, arguments.args.stop, description, task)

elif arguments.args.start != None:
	print(arguments.args.start)
	print('Didn´t enter an end value')
elif arguments.args.stop != None:
	print(arguments.args.stop)
	print("Didnt enter a start value")


# tlx Module

if arguments.args.task:
	if arguments.args.create:
		if arguments.args.name:
			database.create_task(arguments.args.name, arguments.args.description)
	if arguments.args.list:
		database.list_task()

