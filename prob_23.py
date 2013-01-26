
def find_dividors(n):
	divisors = []
	for i in range(1, n/2 + 1):
		if n % i == 0:
			divisors.append(i)
	return divisors

def sum_list(n):
	total = 0
	for i in range(0, len(n)):
		total += n[i]
	return total

def is_abundant(n):
	if sum_list(find_dividors(n)) > n:
		return True
	else:
		return False

def list_abundant():
	a = []
	for i in range(0, 28124):
		if is_abundant(i):
			a.append(i)
	return a

def possible_sums(a):
	sums = []
	for i in range(0, len(a)):
		for j in range(i, len(a)):
			tmp = a[i] + a[j]
			if tmp < 28124: 
				if not tmp in sums: 
					sums.append(tmp)
			else:
				break
	return sums

sums = possible_sums(list_abundant())
#print sums
total = 0
for i in range(0, 28124):
	if not i in sums:
		total += i
print total

