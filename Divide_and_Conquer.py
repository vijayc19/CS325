import sys
from functools import wraps
sys.setrecursionlimit(4000)
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


def memo(func):
    cache = {}
    @ wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def smax(a):
    if len(a) == 1:
        return a[0]
    return max(smax(a[1:]), smax(a[:-1]), sum(a))


#MAIN PROGRAM
outfile = open('MSS_Results.txt', 'w')	#Creates/opens file for output (overwrites existing file of same name)
arrays = scanInput()


for l in arrays:
    a = tuple(l)
    outfile.write("Array being processed: " + str(a) + "\n")
    outfile.write("Maximum sum: " + str(smax(a)) + "\n\n")
   

