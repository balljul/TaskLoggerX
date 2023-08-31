import argparse

# General Information

parser = argparse.ArgumentParser(prog='TaskLoggerX', description='A dockerized Phyton CLI Tool to track and manage your tasks')

# Commands

parser.add_argument('tlx')
parser.add_argument('-s', '--start')
parser.add_argument('-e', '--end')
parser.add_argument('-d', '--description', action='store_true')

args = parser.parse_args()

if args.tlx == 'start':
    print('Starting TaskLoggerX')

