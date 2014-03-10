def make_string(my_list):
	string = ""
	for i in range(0, len(my_list)):
		string += str(my_list[i])
	return string

def make_list(string):
	string = str(string)
	a = []
	for i in range(0, len(string)):
		a.append(string[i])
	return a

maximum = 0
for i in range(0, 100):
	for j in range(0, 100):
		tmp = make_list(i**j)
		local = 0
		for k in range(0, len(tmp)):
			local += int(tmp[k])
		if local > maximum:
			maximum = local
print maximum


