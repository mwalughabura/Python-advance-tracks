def largest_prime_factor(args):
	test = 2
	while args > 1:
		# print test
		if args % test == 0:
			args /= test
		else:
			test += 1

	print test
	return test