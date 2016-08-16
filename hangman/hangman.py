import random
prompt = ">> "

def choose_random_word():
	words = ["the", "quick", "brown", "fox", "jumped"]
	return  random.choice(words)

myword = choose_random_word()

def print_dashes(myword):
	print myword
	dashes = "_ " * len(myword)
	print dashes
	return dashes


def prompt_and_check_input():
	print "Hey buddy guess a letter in the word"
	answer = raw_input(prompt)
	print answer
	dashes = print_dashes(myword)
	if answer in myword:
		print "You got it!"
		listDashes = []
		getIndices = []
		i = len(myword)
		while i > 0:
			listDashes.append("_ ")
			if i == answer:
				getIndices.append(i)
			i-=1

		print getIndices
		print "".join(listDashes)
		dashes = dashes.replace("_ ", answer)
	print dashes


print_dashes(myword)
prompt_and_check_input()