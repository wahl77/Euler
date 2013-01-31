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
	a.sort()
	return a

i = 1

not_found = True
while not_found:
	my_list = []
	for j in range(1,7):
		my_list.append(make_list(i*j))
	for j in range(1,len(my_list)):
	#	print my_list[j-1]
	#	print my_list[j]
	#	print my_list[j-1] == my_list[j]

		if my_list[j-1] != my_list[j]:
			break
		if j == len(my_list)-1:
			print i
			not_found = False
	
	i += 1
