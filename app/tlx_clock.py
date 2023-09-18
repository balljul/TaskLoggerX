from time import localtime, gmtime, strftime
import tlx_cnf

def get_cet_timestamp():
    return strftime("%a, %d %b %Y %H:%M:%S", localtime())

def get_utc_timestamp():
    return strftime("%a, %d %b %Y %H:%M:%S", gmtime())

def output_ct_timestamps():
    print(f"{tlx_cnf.Color.GREEN}CET Timestamp:{tlx_cnf.Color.RESET} {get_cet_timestamp()}")
    print(f"{tlx_cnf.Color.YELLOW}UTC Timestamp:{tlx_cnf.Color.RESET} {get_utc_timestamp()}")
