
# counter for files, directories contained in a root path
# author: Josiah Gillispie
# date: Aug 10, 2014

import os
import sys

args = sys.argv

if len(args) < 2:
    raise IndexError('Too few arguments')
elif len(args) > 2:
    print 'WARNING: Only the first argument is used!'

myPath = args[1]
myDirs = 0
myFiles = 0

for r,p,f in os.walk(myPath):
    myDirs += len(p)
    myFiles += len(f)

print myPath + ' has '+ str(myDirs) + ' directories and ' + str(myFiles) + ' files.'