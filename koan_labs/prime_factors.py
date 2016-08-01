def largest_prime_factor(args):

	if args == 1:
		return 1

	test = 2
	while args > 1:
		# print test
		if args % test == 0:
			args /= test
		else:
			test += 1

	return test