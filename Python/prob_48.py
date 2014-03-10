def get_last_10(n):
	return n % 10000000000

def my_power(a):
	total = 1
	for i in range(0, a):
		total = get_last_10(total * a)
	return total
		

total = 0
for i in range(1, 1001):
	total += my_power(i)	

print get_last_10(total)
	


