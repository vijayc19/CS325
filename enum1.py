#Peter Rissberger
#4/20/15
#Enumeration 1
#CS 325

import sys

array = [1, 2, -7, 4, 5, -2]
length = len(array)
highestSum = 0

#Outer loop increments left index
for left in range(0, length): 
	newSum = array[left]
	print "\nNew left bound is: " + str(newSum)

	#Inner loop increments right index 
	for right in range(left+1, length):
		print "Adding " + str(array[right]) + " to newSum total of " + str(newSum)
		newSum += array[right]
		
		#Check if new summation is correct 
		if newSum > highestSum:
			highestSum = newSum
			print "		Found new highest sum: " + str(newSum)

print "\nFinal highest sum: " + str(highestSum)
