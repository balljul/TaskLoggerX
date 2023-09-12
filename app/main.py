import argparse

# General Information

parser = argparse.ArgumentParser(prog='TaskLoggerX', description='A dockerized Phyton CLI Tool to track and manage your tasks')

# Commands

parser.add_argument('tlx')
# parser.add_argument('tlx', choices=['start', 'end', 'description'], help='Available commands: start, end, description')
parser.add_argument('-s', '--start', action='store_true')
parser.add_argument('-e', '--end', action='store_true')
parser.add_argument('-d', '--description', action='store_true')

args = parser.parse_args()

if args.start == True and args.end == True:
    print('Set start and end to true')
elif args.start == True:
   print('Set start to true')
elif args.end == True:
   print('Set end to true')
elif args.description == True:
    print("TaskLoggerX: A dockerized Phyton CLI Tool to track and manage your tasks")
else:
    print('No command was given')