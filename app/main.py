#import argparse

# General Information

#parser = argparse.ArgumentParser(prog='TaskLoggerX', description='A dockerized Phyton CLI Tool to track and manage your tasks')

# Commands

#parser.add_argument('tlx')
#parser.add_argument('-s', '--start')
#parser.add_argument('-e', '--end')
#parser.add_argument('-d', '--description', action='store_true')

#args = parser.parse_args()

#if args.tlx == 'start':
 #   print('Starting TaskLoggerX')




import argparse
import datetime
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")
parser.add_argument("-l", "--long", action="store_true")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name


for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
