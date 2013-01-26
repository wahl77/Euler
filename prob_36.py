
def is_palindrome(n):
	string = str(n)
	is_palindrome = True
	for i in range(0, len(string)/2):
		if string[i] != string[len(string) - i - 1]:
				return False
	return True

def num_to_binary(n):
	my_num = []
	while n != 0:
		my_num.insert(0,n % 2)
		n = n / 2
	string = ""
	for i in range(0, len(my_num)):
			string += str(my_num[i])
	return string


total = 0
for i in range(1,1000000):
	if is_palindrome(i) == True and is_palindrome(num_to_binary(i)):
		total += i
	
print total



