import time
from time import localtime, gmtime, strftime
import tlx_cnf

def get_local_timestamp():
    return strftime("%a, %d %b %Y %H:%M:%S", localtime())

def get_utc_timestamp():
    return strftime("%a, %d %b %Y %H:%M:%S", gmtime())

def output_ct_timestamps():
	while True:
		print("\033c", end="")

		print(f"{tlx_cnf.Color.GREEN}Local Time:{tlx_cnf.Color.RESET} {get_local_timestamp()}")
		print(f"{tlx_cnf.Color.YELLOW}UTC Time:{tlx_cnf.Color.RESET} {get_utc_timestamp()}")

		time.sleep(0.5)

if __name__ == "__main__":
	output_ct_timestamps()
