from itertools import count

TARGET = 1000000

def is_prime(n):
	if n <= 1:
		return False
	if n == 2 or n == 3 or n == 5: 
		return True
	if n % 2 == 0:
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
	for i in count(3,2):
		if is_prime(i):
			yield i

primes = []
counter = 0

local_max = (0,0)
total = []
for i in next_prime():
	counter += 1
	primes.append(i)
	for j in range(0, len(primes)):
		if sum(primes[j:]) < TARGET:
			if is_prime(sum(primes[j:])) == True and len(primes[j:]) > local_max[1]:
				local_max = (sum(primes[j:]), len(primes[j:]))
	if sum(primes[-local_max[1]:]) >= TARGET:
		break
print local_max



