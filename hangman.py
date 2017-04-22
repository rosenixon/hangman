import urllib2
from random import randint

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = urllib2.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()

numWords = len(WORDS)
x = randint(0, numWords)

word = WORDS[x].lower()

#print(word)

blankWord = [None] * len(word)
for i in range(0,len(word)):
	blankWord[i] = "_"

print(" ".join(blankWord))
count = 0
errorCount = 3
for i in xrange(0, len(word)+2):

	guess = raw_input("Guess a letter: ")

	changed = 0
	for j in range(0, len(word)):
		if guess == word[j]:
			blankWord[j] = guess
			changed = 1
			count+=1

	if changed == 0:
		if errorCount == 1:
			break
		errorCount-=1
		print("Incorrect. " + str(errorCount) + " guess(es) remaining.")
	

	print(" ".join(blankWord))

	if count == len(word):
		print("You won!")
		break

	
if count != len(word):
	print("You lost :( The word was " + word + ".")

