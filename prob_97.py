

def last_digit(a):
	a = a+a
	tmp = str(a)
	if len(tmp) <= 10:
		return int(tmp)
	else:
		return int(tmp[len(tmp)-10:])

i = 0
x = 1
while i < 7830457:
	x = last_digit(x)
	i += 1
tmp = str(28433*x + 1)
print int(tmp[len(tmp)-10:])

