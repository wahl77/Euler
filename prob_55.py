
def is_palindrome(n):
	string = str(n)
	is_palindrome = True
	for i in range(0, len(string)/2):
		if string[i] != string[len(string) - i - 1]:
				return False
	return True

def reverse_number(n):
	number = str(n)
	new_number = 0
	for i in range(1, len(number)+1):
		new_number = 10*new_number + int(number[len(number)-i])
	return new_number

def is_lychrel(n):
	counter = 1
	while not is_palindrome(n + reverse_number(n)):
		counter += 1
		if counter >= 50:
			return True
		n = n + reverse_number(n)
	return False

counter = 0
for i in range(0, 10000):
	if is_lychrel(i):
		counter += 1

print counter




