class Color:
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RESET = '\033[0m'

class db_cnf:
	host = "Host"

	def get_host(self):
		return self.host
