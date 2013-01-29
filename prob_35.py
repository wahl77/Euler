#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

import itertools 

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
	yield 2
	for i in range(3, 1000000, 2):
		if is_prime(i):
			yield i

def shift(my_list, n):
	return my_list[n:]+ my_list[:n]
			
def list_cycle(a):
	string = str(a)
	my_list = []
	for i in range(0, len(string)):
		my_list.append(shift(a,i))
	return my_list

def is_circular(n):
	my_list = list_cycle(str(n))
	for i in range(0, len(my_list)):
		if is_prime(make_int(my_list[i])) == False:
			return False
	return True

circular = []
for i in next_prime():
	if is_circular(i):
		circular.append(i)
print len(circular)
