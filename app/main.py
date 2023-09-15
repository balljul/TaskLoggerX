import argparse
from time import localtime, gmtime, strftime

# General Information
parser = argparse.ArgumentParser(prog='TaskLoggerX', description='A dockerized Phyton CLI Tool to track and manage your tasks')

# Arguments
parser.add_argument('tlx')
parser.add_argument('-s', '--start', dest='start', action='store')
parser.add_argument('-e', '--end', dest='stop', action='store')
parser.add_argument('-d', '--description', dest='desc', action='store_const')
parser.add_argument('-ct', '--current-time', action='store_true', dest='show_time', help='Gives you the current CET and UTC Timestamp')

args = parser.parse_args()


# Logic

class Color:
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RESET = '\033[0m'



if args.show_time:
	current_cet_timestamp = strftime("%a, %d %b %Y %H:%M:%S", localtime())
	current_utc_timestamp = strftime("%a, %d %b %Y %H:%M:%S", gmtime())

	print(f"{Color.GREEN}CET Timestamp:{Color.RESET} {current_cet_timestamp}")
	print(f"{Color.YELLOW}UTC Timestamp:{Color.RESET} {current_utc_timestamp}")

if args.start != None and args.stop != None:
	tf=open("./worktime.txt","r+")
	timedata=tf.readlines()
	timedata_len=len(timedata)
	tf.write(args.start + " | " + args.stop + "\n")
elif args.start != None:
	print(args.start)
	print('Didn´t enter an end value')
elif args.stop != None:
	print(args.stop)
	print("Didnt enter a start value")

if args.desc:
	print(timedata_len)
