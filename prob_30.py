number = 5
upper_limit = 9 ** number
upper_limit *= number

def sum_of_powers(num):
	string = str(num)
	total = 0
	for i in range(0,len(string)):
		total += (int(string[i])**number)
	if total == num:
		return True
	else:
		return False

total = 0
for i in range(2, upper_limit):
	if sum_of_powers(i) == True:
		total += i

print total

