#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

import itertools 
from itertools import count

def make_int(my_list):
	string = ""
	for i in range(0, len(my_list)):
		string += str(my_list[i])
	return int(string)

def make_list(string):
	string = str(string)
	a = []
	for i in range(0, len(string)):
		a.append(string[i])
	return a

def is_prime(n):
	if n <= 1:
		return False
	if n == 2 or n == 3 or n == 5: 
		return True
	if n%2 == 0:
		return False
	else:
		i = 3
		while i <= int((n**0.5)+1):
				if n % i == 0:
					return False
				i += 2
		return True

def  next_prime():
	for i in count(10,1):
		if is_prime(i):
			yield i

def shift_left(num):
	my_list = make_list(num)
	tmp = []
	for i in range(0, len(my_list)):
		tmp.insert(0, list(my_list[:len(my_list)-i]))
	return tmp

def shift_right(num):
	my_list = make_list(num)
	tmp = []
	for i in range(1, len(my_list)+1):
		tmp.insert(0, list(my_list[len(my_list)-i:]))
	return tmp


def is_truncatable(n):
	shift_list = shift_right(n)
	for i in range(0, len(shift_list)):
		if is_prime(make_int(shift_list[i])) == False:
				return False
	
	shift_list = shift_left(n)
	for i in range(0, len(shift_list)):
		if is_prime(make_int(shift_list[i])) == False:
				return False

	return True
	
counter = 0
total = 0
for i in next_prime():
	if is_truncatable(i):
		counter += 1
		total += i
	if counter == 11:
		break
print total
