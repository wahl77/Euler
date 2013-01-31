
matrix = {}
for i in range(1, 1001):
	matrix[i] = 0


for a in range(1, 1000):
	for b in range(a, 1000):
		c = (a*a + b*b)**0.5
		if (a+b+c) > 1000:
			break
			#print "hey"
		if c == int(c):
			matrix[a+b+int(c)] += 1


max_val = 0
for i in range(1,max(matrix)):
	max_val = max(max_val, matrix[i])

for i in range(1,max(matrix)):
	if matrix[i] == max_val:
		print i
