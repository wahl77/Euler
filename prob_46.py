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
	for i in count(3,2):
		if is_prime(i):
			yield i

primes = [2]
i = 9

while True:
	while primes[len(primes)-1] < i:
		for j in next_prime():
			if j not in primes:
				primes.append(j)
				break
		#print primes

	found = False
	if i not in primes:
		for j in range(0, len(primes)):
			if found:
				break
			for k in range(1, int(i**0.5 + 1)):
				if (primes[j] + 2 * k * k) == i:
					#print i, " = ", primes[j], "+ 2x",k,"*",k
					found = True
					break
		if found == False:
			print i
			break

	i += 2


