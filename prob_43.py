from itertools import permutations
def make_string(my_list):
	string = ""
	for i in range(0, len(my_list)):
		string += str(my_list[i])
	return int(string)

a = list(permutations('0123456789'))
total = 0
for i in range(0, len(a)):
	if make_string(a[i][1:4]) % 2 == 0:
		if make_string(a[i][2:5]) % 3 == 0:
			if make_string(a[i][3:6]) % 5 == 0:
				if make_string(a[i][4:7]) % 7 == 0:
					if make_string(a[i][5:8]) % 11 == 0:
						if make_string(a[i][6:9]) % 13 == 0:
							if make_string(a[i][7:10]) % 17 == 0:
								total += make_string(a[i])

print total
