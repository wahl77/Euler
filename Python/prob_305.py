word = []
number_position = []
word_found_times = []

for i in range(1, 14):
	word.append(str(3**i))

for i in range(0, len(word)):
	word_found_times.append(0)

def get_position():
	position = -6
	counter = 1
	found = []
	stream = '0000000' # Keep this 7 characters (3**13)

	not_done = True
	



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
					if word_found_times[i] == int(word[i]):
						number_position.append(position)
						print number_position
			
		if len(number_position) == len(word):
			print number_position
			return number_position
			break
		counter +=1
		


positions = get_position()
print sum(positions)
