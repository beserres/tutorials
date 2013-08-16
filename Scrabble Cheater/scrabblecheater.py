scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}

w = open("sowpods.txt", "r")

wordlist = []
for line in w:
	line = line.strip()
	wordlist.append(line)

print("Welcome to ScrabbleCheater!")
rack = raw_input("Please enter the letters in your Scrabble rack: ")
print("Thanks, I'll use the letters " + rack + " to find the best words.")
if len(rack) > 10:
	print("Are you sure you meant to enter more than 10 characters?")

validWords = []

for word in wordlist:
	candidate = True
	rack_letters = list(rack)
	for letter in word:
		if letter not in rack_letters:
			candidate = False
		else: 
			rack_letters.remove(letter)
	if candidate == True:
		validWords.append(word)
		total = 0
		for letter in word:
			total = total + scores[letter]
		#print word + " " + str(total)
		validWords.append([total, word])

validWords.sort()

for entry in validWords:
	score = entry[0]
	word = entry[1]
	print(str(score)+ " " + word)

#for word in validWords:
#	print("Valid word: %s" % word)