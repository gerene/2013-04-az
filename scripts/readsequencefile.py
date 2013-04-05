# screed can take input files and create a database. 

# save this in the same directory (folder) as the screed data. 
 
#import sys
#import screed 
 
#filename = sys.argv[1] # make script general. special array = argv = command line arguments for a program. 0 (first element) = name of script, so first argument is 1. name of script is available to you 
#print filename

#for record in screed.open(filename): # contains 25000 records
#	print record 
#	break # after printing first record, it stops. --> prints first record, which is a dictionary - which has keys and values. 

#sys.argv  = whatever we've typed onto the commandline.

# short cut for backing up = cd ..

# type this into gitbash cmd: python readsesequencefile.py (this script) ../data/25k.fq.gz

import sys
import screed 
 
filename = sys.argv[1] # make script general. special array = argv = command line arguments for a program. 0 (first element) = name of script, so first argument is 1. name of script is available to you 
print filename

count = 0
for record in screed.open(filename): # contains 25000 records
	count +=1
	if count > 10:
			break # after printing first record, it stops. --> prints first record, which is a dictionary - which has keys and values. 
	print record ['sequence'] # before colon = key, after = value
	