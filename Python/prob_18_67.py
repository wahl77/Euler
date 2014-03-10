#content = [line.strip() for line in open('data18')]
with open("triangle.txt", 'r') as f:
	data = [map(int, line.split()) for line in f]

print data


def max(a,b):
	if a > b:
		return a
	else:
		return b

total = []
total.append(data[0][0])

new_vector = []
new_vector.append(data[1][0]+total[0])
new_vector.append(data[1][1]+total[0])
total.append(new_vector)

new_vector = []
new_vector.append(data[2][0]+total[1][0])
new_vector.append(data[2][1]+max(total[1][0],total[1][1]))
new_vector.append(data[2][2]+total[1][1])
total.append(new_vector)

for i in range (3, len(data)):
	new_vector = []
	new_vector.append(data[i][0]+total[i-1][0])
	for j in range(1, i):
		new_vector.append(data[i][j]+max(total[i-1][j-1],total[i-1][j]))
	new_vector.append(data[i][i]+total[i-1][i-1])
	total.append(new_vector)






maximum=0
for i in range(0, len(total[len(total)-1])):
	if total[len(total)-1][i]>maximum:
		maximum = total[len(total)-1][i]
print maximum
