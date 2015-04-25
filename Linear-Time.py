#Alex C. Way
#4/25/15
#Linear-time
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
	print "\nFinal highest sum: " + str(maxCurrent)
	return maxCurrent


#MAIN PROGRAM
arrays = scanInput()
print "Arrays detected in file: " + str(len(arrays))

#Run the linearTime function on each array and output the results to 'MSS_Results.txt'
outfile = open('MSS_Results.txt', 'w')	#Creates/opens file for output (overwrites existing file of same name)

for x in range(len(arrays)):
	outfile.write("Array being processed: " + str(arrays[x]) + "\n")
	outfile.write("Final highest sum: " + str(linearTime(arrays[x])) + "\n\n")
