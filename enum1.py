#Peter Rissberger
#4/20/15
#Enumeration 1
#CS 325

import sys


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
	

def enum1(array):
	maxI = 0
	maxJ = 0
	maxSubarray = []
	highestSum = 0	#Highest subarray sum yet found
	length = len(array)

	#Special case for length 1 arrays
	if length == 1:
		#print "\nFinal highest sum: " + str(array[0])
		outfile.write("Maximum subarray: " + str(array) + "\n")
		outfile.write("Maximum sum: " + str(array[0]) + "\n\n")
		return		

	#Outer loop increments left index
	for left in range(0, length): 
		newSum = array[left]
		#print "\nNew left bound is: " + str(newSum)

		#Inner loop increments right index 
		for right in range(left+1, length):
			#print "Adding arrays " + str(left) + " through " + str(right)
			newSum = 0
			
			marker = left
			while marker <= right:
				newSum += array[marker]
				marker += 1
				#print "Adding " + str(array[marker]) + " = " + str(newSum)

				#Check if new summation is the new maximum
				if newSum > highestSum:
					highestSum = newSum
					maxI = left
					maxJ = marker

	#Print maximum subarray to outfile
	for y in range(maxI, maxJ):
		maxSubarray.append(array[y])

	outfile.write("Maximum subarray: " + str(maxSubarray) + "\n")
	outfile.write("Maximum sum: " + str(highestSum) + "\n\n")	

	
#MAIN PROGRAM
outfile = open('MSS_Results.txt', 'w')	#Creates/opens file for output (overwrites existing file of same name)
arrays = scanInput()

outfile.write("Arrays detected in file: " + str(len(arrays)) + "\n\n")

#Run the enum1 file on each array and output the results to 'MSS_Results.txt'
for x in range(len(arrays)):
	outfile.write("Array being processed: " + str(arrays[x]) + "\n\n")
	enum1(arrays[x]) #Enum1 prints the maximum subarray here
	
