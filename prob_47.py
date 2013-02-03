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

i = 1
while True:
	array[i % LENGTH] = get_factor(i)
	i += 1
	All_Length = True
	for j in range(0, len(array)):
		if len(array[j]) != LENGTH:
			All_Length = False
			break



	if All_Length == True:
		print array
		print i-LENGTH
		break
