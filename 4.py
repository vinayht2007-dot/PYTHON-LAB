import os.path
import sys
fname = input("enter the file name to sort:")
if  not os.path.isfile(fname):
    print("file not found")
    sys.exit(0)
infile.close()
lineList = []
for line in lines:
    lineList.append(line.strip())
lineList.sort()
outfile = open("sorted.txt","w+")
if not os.path.isfile(fname):
    print("not able to create sorted.txt")
    sys.exit(0)
for line in lineList:
    outfile.write(line + "\n")
outfile.close()
print("sorted.txt created successfully")