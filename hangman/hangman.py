import random
prompt = ">> "
hangman = {

	"full":"""
	  ______
	 |      |
	 |      0
	 |     /|\
	 |     / \
	 |
	""",
	"poll":"""
	  ______
	 |
	 |
	 |
	 |
	 |
	""",
	"rope":"""
	  ______
	 |      |
	 |
	 |
	 |
	 |
	""",
	"head":"""
	  ______
	 |      |
	 |		0
	 |
	 |
	 |
	""",
	"frontLimbs":"""
	  ______
	 |      |
	 |		0
	 |     / \
	 |
	 |
	""",
	"body":"""
	  ______
	 |      |
	 |		0
	 |     /|\
	 |
	 |
	""",
	"start":"""
	  
	 |
	 |
	 |
	 |
	 |
	"""
}

def choose_random_word():
	words = ["the", "quick", "brown", "fox", "jumped","over","lazy","dog"]
	return  random.choice(words)

myword = choose_random_word()

def print_dashes(myword):
	print myword
	dashes = "_ " * len(myword)
	print dashes
	return dashes


def prompt_and_check_input():
	# attempts = 8
	# while attempts >= 0:
	# 	attempts-=1
	print "Hey buddy guess a letter in the word"
	answer = raw_input(prompt)
	print answer
	dashes = print_dashes(myword)
	myWordInList = list(myword)

	if answer in myWordInList:
		listDashes = list("_" * len(myword))
		i = len(myWordInList) - 1
		while i >= 0:
			if myWordInList[i] == answer:
				listDashes[i] = answer
			i-=1
		print "".join(listDashes)

	else:
		print "You have lost"


print_dashes(myword)
prompt_and_check_input()