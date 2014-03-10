import math
from itertools import count

def solve_quadratic(a,b,c):
	a = 1.0 * a
	b = 1.0 * b
	c = 1.0 * c

	tmp = b ** 2 - 4*a*c
	
	if tmp < 0:
		return (0, 0)
	else:
		res1 = -b + math.sqrt(b ** 2 - 4*a*c)
		#res2 = -b - math.sqrt(b ** 2 - 4*a*c)
	return res1/(2*a)
	#return (res1/(2*a), res2/(2*a))


def Triangle(n):
	return solve_quadratic(1,1,-2*n)

def Pet(n):
	return solve_quadratic(3, -1, -2*n)

def next_hex():
	for i in count(144, 1):
		yield i*(2*i-1)

for i in next_hex():
	if Triangle(i) == int(Triangle(i)) and Pet(i) == int(Pet(i)):
			print i
			break


