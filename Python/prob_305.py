def get_position(word):
	position = -6
	counter = 1
	found = []
	stream = '0000000' # Keep this 7 characters (3**13)

	not_done = True
	number_position = []
	word_found_times = []
	

	for i in range(0, len(word)):
		word_found_times.append(0)


	while not_done:
		# Update Stream
		for j in range(0, len(str(counter))): 
			position += 1
			stream = stream[len(str(stream))-6:]+str(counter)[j]

			for i in range(0, len(word)):
				found_word = True
				for j in range(0, len(word[i])):
					if word[i][j] != str(stream[j]):
						found_word = False
						break
				if found_word == True:
					word_found_times[i] += 1
					print "Found word ", word[i], " at position", position
					#if word_found_times[i] == 1:#int(word[i]):
					if word_found_times[i] == int(word[i]):
						number_position.append(position)
						print number_position
			
		if len(number_position) == len(word):
			print number_position
			return number_position
			break
		counter +=1
		


def prob_305():
	word = []
	for i in range(1, 14):
		word.append(str(3**i))
	positions = get_position(word)
	print sum(positions)


def test(n):
	word = []
	i = 2
	word.append(str(n))
	positions = get_position(word)
	print sum(positions)

test(9)
test(15)
test(16)
test(3**13)
