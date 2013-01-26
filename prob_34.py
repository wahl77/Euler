def fact(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	else:
		return n * fact(n-1)

def is_curious(n):
	number = str(n)
	total = 0
	for i in range(0, len(number)):
			total += fact(int(number[i]))

	if total == n:
		return True
	else:
		return False



# 7*9! is upper limit because 9'999'999 > 7*9!
total = 0
for i in range(3, 7*fact(9)): 
	if is_curious(i):
		total += i
		print total, i
	i += 1


