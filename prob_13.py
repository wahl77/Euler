with open("prob_13.txt", 'r') as f:
	data = [map(int, line.split()) for line in f]

total = 0
a=[]
for j in range(50,0,-1):
	for i in range(0, len(data)):
		 total += int(str(data[i])[j])
	a.append(total % 10)
	total = total / 10

a.append(total)
a.reverse()

# Make a single string:
tmp =""
for i in range(0,len(a)):
	tmp += str(a[i])
print tmp[:10]



	
# If can do large integer additions
total = 0
for i in range(0,len(data)):
	total += data[i][0]

print total



