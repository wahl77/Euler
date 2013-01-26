import re # Just for removing white space
import sys

numbers = {1: "one", 2:"two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14:"fourteen", 15: "fifteen", 16:"sixteen", 17:"seventeen", 18: "eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40: "forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred"}


def print_value(n):
	string = ""
	if n > 999:
		string += numbers[n / 1000] + " " 
		string += "thousand "
		n = n % 1000
	if n > 99:
		string += numbers[n / 100] + " "
		string += "hundred "
		if n % 100 != 0:
			string +="and "
		else:
			return string
		n = n % 100
	if n >= 20:
		string += numbers[(n/10) * 10] + " "
		n = n % 10
	if n < 20 and n != 0:
		string += numbers[n] + " "
	

	return string
	

def prob_17():
	total = 0
	for i in range(1, 1001):
		total += len(print_value(i).replace(' ','')) # .replace(' ', '') is just for removing the white spaces
	print total

if len(sys.argv) == 1:
	prob_17()
else:
	print print_value(int(sys.argv[1]))
