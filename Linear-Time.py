#Alex C. Way
#4/26/15
#Linear-time
#CS 325

import sys
from random import randint

def randArray():
	array = []
	n = int(sys.argv[1])
	#outfile = open('randArray.txt', 'w')	#Outfile used to store array

	#Append 'n' random integers between -99 and 99 to array
	for x in range(n):
		array.append(randint(-99,99))

	#outfile.write(str(array))
	return array

#Scans 'MSS_Problems.txt' and returns an array of arrays contained in the file
def scanInput():
	infile = open('MSS_Problems.txt', 'r')	#File containing all arrays to be tested
	outfile = open('MSS_Results.txt', 'w')	#Outfile used as a temp file for arrays

	#Cleanup junk brackets and commas from file 
	string = infile.read()
	string = string.translate(None, '[],') 	#Clean up junk commas and brackets from input
	outfile.write(string)
	outfile.seek(0)
		
	#Make array of arrays contained in infile
	with open('MSS_Results.txt') as f: 
		outerArray = []
		for line in f: 
			line = line.split() 
			if line: 
				line = [int(i) for i in line]
				outerArray.append(line)

	#Clean up outfile used as temp work file
	outfile.truncate(0)
	outfile.close()

	return outerArray


def linearTime(array):
	maxCurrent = 0
	maxSuffix = 0
	for i in range (0, len(array)):
		maxSuffix = maxSuffix + array[i]
		#print "\n maxSuffix: " + str(maxCurrent)
		#print "\n array[i]: " + str(array[i])
		if maxSuffix < 0:
			maxSuffix = 0
		if maxCurrent < maxSuffix:
			maxCurrent = maxSuffix
	#print "\nFinal highest sum: " + str(maxCurrent)
	return maxCurrent


#MAIN PROGRAM


#Run the linearTime function on each array and output the results to 'MSS_Results.txt'
outfile = open('MSS_Results.txt', 'w')	#Creates/opens file for output (overwrites existing file of same name)

if int(sys.argv[1]) > 0:
	totalTime = 0
	for x in range(10):
		theRandArray = randArray()
		highestSum = str(linearTime(theRandArray))
		outfile.write("Array being processed: " + str(theRandArray) + "\n")
		outfile.write("Final highest sum: " + highestSum + "\n\n")
		print("\nFinal highest sum: " + highestSum)
		if __name__ == '__main__':
			import timeit
			timeVal = timeit.timeit("linearTime(theRandArray)", setup="from __main__ import linearTime, theRandArray, x", number=1)
			totalTime += timeVal
			print("The timing was: ")
			print(timeVal)
			print(" seconds.")
	print "average time is: "
	print totalTime/10
else:
	arrays = scanInput()
	print "Arrays detected in file: " + str(len(arrays))
	for x in range(len(arrays)):
		highestSum = str(linearTime(arrays[x]))
		outfile.write("Array being processed: " + str(arrays[x]) + "\n")
		outfile.write("Final highest sum: " + highestSum + "\n\n")
		print("\nFinal highest sum: " + highestSum)
		if __name__ == '__main__':
			import timeit
			print("The timing was: ")
			print(timeit.timeit("linearTime(arrays[x])", setup="from __main__ import linearTime, arrays, x", number=1))
			print(" seconds.")
