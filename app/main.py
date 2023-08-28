import argparse

print('Docker Container is running')

print(proc.stdout)
# General Information

parser = argparse.ArgumentParser(prog='TaskLoggerX', description='A dockerized Phyton CLI Tool to track and manage your worktime')

# Commands

parser.add_argument('tlx')
parser.add_argument('-s', '--start')
parser.add_argument('-e', '--end')
parser.add_argument('-d', '--description', action='store_true')

args = parser.parse_args()
print(args.tlx, args.start, args.end, args.description)

if args.tlx == 'start':
    print('Starting TaskLoggerX')

