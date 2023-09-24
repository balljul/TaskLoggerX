import argparse

# General Information
parser = argparse.ArgumentParser(prog='TaskLoggerX', description='A dockerized Phyton CLI Tool to track and manage your tasks')

# Arguments
parser.add_argument('tlx')
parser.add_argument('-s', '--start', dest='start', action='store', type=int)
parser.add_argument('-e', '--end', dest='stop', action='store', type=int)
parser.add_argument('--current-time', action='store_true', dest='show_time', help='Gives you the current CET and UTC Timestamp')
parser.add_argument('-d', '--description', action="store", dest='description', help='Lets you add a description')
parser.add_argument('-l', '--list', action="store_true", dest='list', help='List entries')

parser.add_argument('-t', '--task', action='store_true', dest='task', help='Create a task')
parser.add_argument('-c', '--create', action='store_true', dest='create', help='Create Mode')
parser.add_argument('-n', '--name', action='store', dest='name', help='Set a name')
parser.add_argument('-a', '--append', action='store', dest='append', help=argparse.SUPPRESS )

parser.add_argument('--database-show', action='store_true', dest='dbshow',  help='Shows all tables in the database')
parser.add_argument('--database-migrate', action='store_true', dest='dbmigrate', help='Migrates the database')
parser.add_argument('--database-drop', action='store_true', dest='dbdrop', help='A quick way to drop all tables in the database')
parser.add_argument('--database-seed', action='store_true', dest='dbseed', help='Seeds the database')
args = parser.parse_args()
