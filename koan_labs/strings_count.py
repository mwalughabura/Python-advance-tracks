def count_letter_b(string):
	#TODO: Your code goes here
	stringList = []

	i = len(string) - 1
	while i >= 0:
		stringList+=string[i]
		i-=1

	beezInTheTrap = []
	for i in stringList:
		if ord(i) == ord('b') or ord(i) == ord('B'):
			beezInTheTrap.append(i)

	return len(beezInTheTrap)