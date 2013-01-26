total = 0
a, b = 0, 1
while (a+b) < 4000000:
	a,b = b,(a+b)
	if b % 2 == 0:
		total += b

print total
