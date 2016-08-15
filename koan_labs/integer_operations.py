def integer_operations(initial_value):
	#TODO: Your code goes here
	lastFive = []
	increase= initial_value + 5

	while initial_value <= increase:
		lastFive.append(initial_value)
		initial_value+=1
	# initial = lastFive.pop(0)
	return sum(lastFive)# + initial
