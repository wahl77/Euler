def make_string(my_list):
	string = ""
	for i in range(0, len(my_list)):
		string += str(my_list[i])
	return string

def make_list(string):
	string = str(string)
	a = []
	for i in range(0, len(string)):
		a.append(string[i])
	return a

def is_pandigital(array):
	total_length = 0
	numbers_as_list = []

	for i in range(0, len(array)):
		total_length += len(str(array[i]))
	
	for i in range(0, len(array)):
		number = make_list(array[i])
		for j in range(0,len(number)):
			numbers_as_list.append(number[j])

	for i in range(1, len(numbers_as_list)+1):
		if str(i) not in numbers_as_list:
			return (False, 0)
	return (True, total_length) 

# The following can be optimized drastically
pan_numbers = []
for i in range(0, 100):
	for j in range(i,9999):
		if is_pandigital([i, j, i*j]) == (True, 9):
			if (i*j) not in pan_numbers:
				pan_numbers.append(i*j)
print sum(pan_numbers)
