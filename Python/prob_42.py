import re
import itertools

with open("prob_42.txt", 'r') as f:
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

def triangle_list(max_value):
	my_list = []
	i = 1
	tmp = 1
	while tmp <= max_value:
		tmp = i * (i+1)/2
		my_list.append(tmp)
		i +=1
	return my_list


word = []
for i in range(0, len(data[0])):
 word.append(value_of_string(data[0][i]))

triangle_set = triangle_list(max(word))
counter = 0
for i in range(0, len(word)):
	if word[i] in triangle_set:
		counter += 1
print counter
