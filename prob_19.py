import datetime
from datetime import date

counter = 0
for year in range(1901, 2001):
	for month in range(1, 13):
		try: 
			if date(year,month,1).weekday() == 6 :
				counter += 1
		except ValueError:
			continue

print counter



