
def is_palindrome(n):
	string = str(n)
	is_palindrome = True
	for i in range(0, len(string)/2):
		if string[i] != string[len(string) - i - 1]:
				return False
	return True

largest = 0
for i in range(999, 0, -1):
	for j in range(999, 0, -1):
		if is_palindrome(i*j) and (i*j) > largest:
			largest =  i*j

print largest


