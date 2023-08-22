import argparse

print('Docker Container is running')


# General Information

parser = argparse.ArgumentParser(
    prog='TaskLoggerX',
    description='A dockerized Phyton CLI Tool to track and manage your worktime'
)

# Commands

parser.add_argument(
    'startDay',
    action='store_true', 
    help='Starts a new day'                
)

print(parser.parse_args())