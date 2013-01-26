from itertools import count
def chain_length(num):
	counter = 1
	while num != 1:
		if num % 2 == 0:
			num /= 2
		else:
			num = (3*num) + 1
		counter += 1
	return counter

longest = 1
seq_length = 1
for i in range(1,1000000):
	if chain_length(i) > seq_length:
		longest = i
		seq_length = chain_length(i)
	if i > 1000000:
		break
print longest
	
	
