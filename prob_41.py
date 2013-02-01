import itertools 
from itertools import count
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

def is_prime(n):
	if n <= 1:
		return False
	if n == 2 or n == 3 or n == 5: 
		return True
	else:
		i = 3
		while i <= int((n**0.5)+1):
				if n % i == 0:
					return False
				i += 2
		return True

# 9+8+7+6+5+4+3+2+1 % 3 = 0
# 8+7+6+5+4+3+2+1 % 3 = 0
i = 7654321
while True:
	if is_pandigital([i])[0] == True:
		if is_prime(i):
			print i
			break
	i -= 2
	
