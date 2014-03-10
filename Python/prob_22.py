import re

with open("prob_22.txt", 'r') as f:
	data = [map(str, line.split(",")) for line in f]

data[0].sort()

def value_of_char(a):
	return ord(a) - ord('A') + 1

def value_of_string(string):
	string = string.replace('"','')
	total = 0
	for i in range(0,len(string)):
		total += value_of_char(string[i])
	return total

total = 0
for i in range(0, len(data[0])):
	total += (i+1)*value_of_string(data[0][i])

print total
