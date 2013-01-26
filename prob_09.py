def is_pyth(a,b,c):
	if a*a + b*b == c*c:
		return True
	else:
		return False

for i in range(1,1000):
	for j in range(i,1000):
		k = 1000-i-j
		if is_pyth(i,j,k):
			print i*j*k
