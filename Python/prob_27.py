#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

import itertools 


def is_prime(n):
	if n <=1:
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

def get_primes():
	a = []
	for i in range(3, 1000000, 2):
		if is_prime(i):
			a.append(i)
	a.insert(0,2)
	return a


def formula(a,b):
		i = 0
		a,b = int(a), int(b)
		count = 0
		while True:
			if is_prime(i**2 + a*i + b):
				count += 1
				i += 1
			else:
				break;
		return [count, a, b]

maximum = [0,0,0]
for a in range(-1000, 1000):
	for b in range(-1000, 1000):
		tmp = formula(a,b)
		if tmp[0] > maximum[0]:
			maximum = tmp 

print maximum
print maximum[1]*maximum[2]
			
