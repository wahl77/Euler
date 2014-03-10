def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)

def choose(n,r):
	return fact(n)/(fact(r)*fact(n-r))

print choose(40,20)

