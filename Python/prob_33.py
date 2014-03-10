def make_string(my_list):
	string = ""
	for i in range(0, len(my_list)):
		string += str(my_list[i])
	return string

def make_list(string):
	string = str(string)
	a = []
	for i in range(0, len(string)):
		a.append(string[i])
	return a


def is_curious(a,b):
	c,d = simplify(a,b)
	a = 1.0 * a
	b = 1.0 * b
	if (a/b) == (c/d) and a != c and b != d and a < b:
		return True
	else:
		return False

def simplify(a,b):
	
	a = make_list(a)
	b = make_list(b)
	for i in range(0, len(a)):
		if a[i] in b:
			b.remove(a[i])
			a.remove(a[i])
			break
	return (1.0*int(make_string(a)), 1.0*int(make_string(b)))

# Bad way but can't be asked right now
def gcd(a,b):
	if a < b:
		a,b = b,a
	val = 1
	for i in range(1, b+1):
		if a % i == 0 and b % i == 0:
			val = i
	return val
	
num = 1
dem = 1
count = 0
for i in range(10, 100):
 for j in range(10, 100):
	if i != j and i%10 != 0 and j % 10 != 0:
		if is_curious(i,j):
			num *= i
			dem *= j
			count += 1
dem /= gcd(num, dem)
print dem


