remainder = 600851475143
prime = 2

while remainder != 1:
	if remainder % prime == 0:
		remainder /= prime
	else:
		prime += 1
print prime
