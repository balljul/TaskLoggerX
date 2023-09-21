import argparse

# General Information
parser = argparse.ArgumentParser(prog='TaskLoggerX', description='A dockerized Phyton CLI Tool to track and manage your tasks')

# Arguments
parser.add_argument('tlx')
parser.add_argument('-s', '--start', dest='start', action='store', type=int)
parser.add_argument('-e', '--end', dest='stop', action='store', type=int)
parser.add_argument('-ct', '--current-time', action='store_true', dest='show_time', help='Gives you the current CET and UTC Timestamp')
parser.add_argument('-d', '--description', action="store", dest='description', help='Lets you add ')

parser.add_argument('-dbs', '--database-show', action='store_true', dest='dbshow',  help='Shows all tables in the database')
parser.add_argument('--database-migrate', action='store_true', dest='dbmigrate', help='Migrates the database')
parser.add_argument('--database-drop', action='store_true', dest='dbdrop', help='A quick way to drop all tables in the database')
parser.add_argument('--database-seed', action='store_true', dest='dbseed', help='Seeds the database')
args = parser.parse_args()
