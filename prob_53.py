def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

def choose(n,r):
	return fact(n)/(fact(r)*fact(n-r))

print choose(23,10) > 1000000
counter = 0
for i in range(1, 101):
	for j in range(0, i+1):
		if choose(i, j) > 1000000:
			counter += 1
print counter

