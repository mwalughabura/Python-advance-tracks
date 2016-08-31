import sqlite3

class Customer(object):
	"""docstring for Customer"""
	def __init__(self, first_name, second_name, id_no):
		self.first_name = first_name
		self.second_name - second_name
		self.id_no = id_no
		

def input_cridential():
	first_name = raw_input("First name: ")
	second_name = raw_input("Second name: ")
	id_no = input("your ID: ")
	while len(str(id_no)) != 4:
		print "Check out your ID"
		id_no = input("your ID: ")


def welcome():
	con = sqlite3.connect("my.db")
	cur = con.cursor()
	cur.execute("select sqlite_version();")

	data = cur.fetchone()

	print data

	con.close()
	# print "Hello Welcome to our Bank!\tThe bank of your choice!"
	# print "\t\tWe are glad to have you here"

	# print "\n\nTo join you can follow the following step"
	# input_cridential()

if __name__ == '__main__':
	welcome()