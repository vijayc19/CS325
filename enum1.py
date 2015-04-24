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
	print "Processing array: " + str(array) + "\nLength: " + str(len(array))
	highestSum = 0	#Highest subarray sum yet found
	length = len(array)

	#Special case for length 1 arrays
	if length == 1:
		print "\nFinal highest sum: " + str(array[0])
		return array[0]

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

				#Check if new summation is correct 
				if newSum > highestSum:
					highestSum = newSum
					print "		Found new highest sum: " + str(newSum)

	print "\nFinal highest sum: " + str(highestSum)
	return highestSum



#MAIN PROGRAM
arrays = scanInput()
print "Arrays detected in file: " + str(len(arrays))

#Run the enum1 file on each array and output the results to 'MSS_Results.txt'
outfile = open('MSS_Results.txt', 'w')	#Creates/opens file for output (overwrites existing file of same name)

for x in range(len(arrays)):
	outfile.write("Array being processed: " + str(arrays[x]) + "\n")
	outfile.write("Final highest sum: " + str(enum1(arrays[x])) + "\n\n")
