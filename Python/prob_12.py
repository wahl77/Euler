from itertools import count
import math

def num_divisors(remainder):
	dividors = 1
	if remainder == 1 or remainder == 0:
		return dividors 

	for i in range (2, int(math.sqrt(remainder))+1):
		if remainder % i == 0:
			dividors += 1

	if math.sqrt(remainder) == int(math.sqrt(remainder))/1.0:
		return 2*dividors - 1
	else:
		return 2*dividors


def next_triangle():
	for i in count(start=1,step=1):
		yield i * (i+1)/2

for i in next_triangle():
	if num_divisors(i) > 500:
		print i
		break
