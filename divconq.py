import sys


#Scans 'MSS_Problems.txt' and returns an array of arrays contained in the file
def scanInput():
    infile = open('MSS_Problems.txt', 'r')	
    outfile = open('MSS_Results.txt', 'w')	

	
    string = infile.read()
    string = string.translate(None, '[],') 
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

def maxSubarray (array, start, end):
    start = 0
    end =  len(array)
    middle = (start + end)/2
    length = len(array)
	
    leftSum = - sys.maxint - 1
    rightSum = - sys.maxint - 1
    sumOne = 0	
    sumTwo = 0
    maxI = 0
    maxJ = 0
    maxSubarray1 = []

    #Special case for length 1 arrays
    if length == 1:
        print "\nFinal highest sum: " + str(array[0])
        return array[0]
   
    leftMSS = maxSubarray(array, start, middle)
    rightMSS = maxSubarray(array+middle, middle+1, end)

	
    for left in range(start, middle -1):
        sumTwo += array[left]
        leftSum = max(leftSum, sumTwo)
        maxI = left
        print 'Left Sum'
        print leftSum
	
    for right in range(middle, end):
        sumOne += array[right] 
        rightSum = max(rightSum, sumOne)
        maxJ = right
        print 'Right Sum'
        print rightSum
			
	#Print maximum subarray to outfile
    for y in range(maxI, maxJ):
        maxSubarray.append(array[y])

    answer = max(leftMSS, rightMSS)
    result = max(answer, leftSum+rightSum) 
	
    outfile.write("Maximum subarray: " + str(maxSubarray1) + "\n")
    outfile.write("Maximum sum: " + str(result) + "\n\n")	
	
    return max(answer, leftSum+rightSum)
	
#MAIN PROGRAM
outfile = open('MSS_Results.txt', 'w')	#Creates/opens file for output (overwrites existing file of same name)
arrays = scanInput()

outfile.write("Arrays detected in file: " + str(len(arrays)) + "\n\n")

#Run the enum1 file on each array and output the results to 'MSS_Results.txt'
for x in range(len(arrays)):
    outfile.write("Array being processed: " + str(arrays[x]) + "\n")
    maxSubarray(arrays[x], 0, len(arrays))
