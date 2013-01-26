amicable_pair = []

def find_dividors(n):
	divisors = []
	for i in range(1, n/2 + 1):
		if n % i == 0:
			divisors.append(i)
	return divisors

def sum_divisors(n):
	total = 0
	divisors = find_dividors(n)
	for i in range(0, len(divisors)):
		total += divisors[i]
	return total

def is_amicable(a,b):
	if a == b:
		return False
	if sum_divisors(a) == b and sum_divisors(b) == a:
		return True
	else:
		return False

def has_amicable_number(a):
	if is_amicable(a, sum_divisors(a)):
		return True
	else:
		return False

for i in range (1, 10000):
	if has_amicable_number(i):
		amicable_pair.append(i)

print amicable_pair

sum_amicable = 0

for i in range(0, len(amicable_pair)):
	sum_amicable += amicable_pair[i]

print sum_amicable
