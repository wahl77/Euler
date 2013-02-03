LENGTH = 4
def get_factor(n):
	primes = []
	prime = 2
	remainder = n
	while remainder != 1:
		if remainder % prime == 0:
			if prime not in primes:
				primes.append(prime)
			remainder /= prime
		else:
			prime += 1
	return primes


	
array = []
for i in range(0, LENGTH):
	array.append([])

i = 0
counter = 0
while True:
	i += 1
	factors = get_factor(i)
	if len(factors) == LENGTH:
		array[i % LENGTH] = factors
		counter += 1
	else:
		counter = 0
	if counter == LENGTH:
		print i-LENGTH+1
		break


