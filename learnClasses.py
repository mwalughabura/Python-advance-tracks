class person(object):
	"""docstring for person"""
	def __init__(self, first_name, second_name):
		super(person, self).__init__()
		self.first_name = first_name
		self.second_name = second_name

	def my_names(self):
		print "My nam is %s %s"%(self.first_name, self.second_name)

student1 = person("mwalugha", "ramadhan")

print student1.my_names()