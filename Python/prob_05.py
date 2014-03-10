def prob_5():
	i = 20
	while True:
		a = False
		for j in range(2,21):		
			if i % j != 0:
				a = True
				break
		if a == False:
			return i
		i += 20

print prob_5()
