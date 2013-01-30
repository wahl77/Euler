coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

matrix = {}
for i in range(0, target+1):
	matrix[i, 0] = 1

for i in range(0, target+1):
	print i, ":", 1, 
	for j in range(1, len(coins)):
		matrix[i,j] = 0
		if i < coins[j]:
			matrix[i,j] = matrix[i, j-1]
		else:
			# Solve the issue by thinking at the problem the following way. Using only
			# coins up to coins[j], how many ways can it be done. Fill in table like that
			matrix[i,j] = matrix[i, j-1]
			matrix[i,j] += matrix[i - coins[j], j]
		print matrix[i,j], 
	print

print matrix[max(matrix)]

