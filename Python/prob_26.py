
def cycle_length(i,j):
 i *= 1.0  
 j *= 1.0  
 remainder = []
 dividor = []
 i = get_10_higher(i,j)
 while (i % j) != 0:
	 if (i % j) not in remainder:
		 remainder.append(int(i) % int(j))
		 dividor.append(int(i)/int(j))
	 else:
		 tmp = i%j
		 count = 0
		 while tmp != remainder[count]:
			 count += 1
		 return len(dividor) - count 
	 times = get_10_higher(i % j,j)
	 i = (int(i)%int(j)) * 10**times
	 for k in range(0,times-1):
		 dividor.append(0)
 return 0

def get_10_higher(i, j):
 times = 0
 while i < j:
	 i *= 10
	 times += 1
 return times

maximum = 0
tmp = 1
for i in range(1, 1000):
	local = cycle_length(1, i)
	if (local > maximum):
		maximum = local
		tmp = i
print tmp

