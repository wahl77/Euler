i = 0
count = 1
length = 0

mult = 1
x = ""
while i < 1000000:
  x += str(i)
  i +=1

for j in range(0, 7):
  mult *= int(x[10**j])

print mult
