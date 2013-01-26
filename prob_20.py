def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)


tmp = str(fact(100))
total = 0

for i in range(0, len(tmp)):
	total += int(tmp[i])

print total
	

