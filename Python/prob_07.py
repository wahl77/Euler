import math
def is_prime(n):
	if n == 1:
		return False
	if n == 2 or n == 3 or n == 5: 
		return True
	else:
		i = 3
		while i <= int(math.sqrt(n)):
				if n % i == 0:
					return False
				i += 2
		return True


counter = 1
number = 3


while counter < 10001:
	if is_prime(number) == True:
		counter += 1
	number += 2

print number - 2

