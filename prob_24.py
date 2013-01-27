import itertools

def make_string(my_list):
	string = ""
	for i in range(0, len(my_list)):
		string += str(my_list[i])
	return string


print make_string(list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))[999999])

