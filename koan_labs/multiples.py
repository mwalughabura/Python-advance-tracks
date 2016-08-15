def multiple_sum():
	listOfNumbers = []

	number = 0
	while number < 1000:
		if number % 3 == 0 or number % 5 == 0:
			listOfNumbers.append(number)

		number+=1

	return sum(listOfNumbers)