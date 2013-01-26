
total = 1

for i in range (3, 1002, 2):
	total +=  4*i*i - 6*i + 6

print total


# can be written as the sum of the following with n increasing two by two

#		n*n-(n-1)		  n*n
#		n*n-2(n-1)		n*n-3(n-1)

# which is n*n + n*n - (n-1) + n*n - 2(n-1) + n*n - 3(n-1)
# = 4*n*n - 6n + 6
		
