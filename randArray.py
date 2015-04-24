#Peter Rissberger
#4/23/15
#Random Array Generator
#CS 325

import sys
from random import randint

array = []
n = int(sys.argv[1])
outfile = open('randArray.txt', 'w')	#Outfile used to store array

#Append 'n' random integers between -99 and 99 to array
for x in range(n):
	array.append(randint(-99,99))

outfile.write(str(array))
