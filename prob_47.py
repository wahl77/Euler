LENGTH = 4
def get_factor(n):
	primes = []
	prime = 2
	remainder = n
	while remainder != 1:
		if remainder % prime == 0:
			if prime not in primes:
				primes.append(prime)
				if len(primes) > LENGTH :
					return LENGTH + 1
			remainder /= prime
		else:
			prime += 1
	return len(primes)

i = 0
counter = 0
while True:
	i += 1
	if get_factor(i) == LENGTH:
		counter += 1
	else:
		counter = 0
	if counter == LENGTH:
		print i-LENGTH+1
		break


