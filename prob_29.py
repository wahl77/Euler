my_list = []

for a in range(2,101):
	for b in range(2, 101):
		new_number = a**b
		if not new_number in my_list:
			my_list.append(new_number)

print len(my_list)
