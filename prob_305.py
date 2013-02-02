looking_for = []

for i in range(0, 14):
	looking_for.append(3**i)

print looking_for


def get_position(n):
	position = -6
	i = 1
	find = str(n)
	found = 0
	stream = '0000000' # Keep this 7 characters (3**13)
	not_done = True
	while not_done:
		for j in range(0, len(str(i))):
			position += 1
			stream = stream[len(str(stream))-6:]+str(i)[j]
			found_word = True
			#print position, stream
			for j in range(0, len(find)):
				if str(find)[j] != str(stream)[j]:
			#		print "Not here: ", stream
					found_word = False
					break
			if found_word == True:
				found += 1
				#print int(find), found
				if found == int(find): 
					print position, stream
					not_done = False 
					return position
					break
					
		i += 1

print get_position(1)
print get_position(5)
print get_position(12)
print get_position(7780)


