def compounded_principal(time):
	# a = p (1 + (r/n)) ^ nt
	# Where:
	# p is the principal amount
	# r is the annual nominal interest rate
	# n is the number of times the interest in compounded per year 
	# t is the number of years
	p = 10000
	r = 0.08
	n = 1

	# a = p (1 + (r/n)) ^ nt
	amount = p * (1 + (r/n)) ** (time * n)

	return int(amount)