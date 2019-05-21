# Aztecs
# Behram Dossabhoy, Matthew Greene, Prasil Mainali, Logan Mccarthy, Joshua Mendoza, Louis Miller, Tracy Samanie
# 29 March 2019
# Binary Decoder: Decode a string of binary, either in base-7 or base-8
# Github: https://github.com/greene-matthew/Team-Aztecs



import sys
import re

file = re.sub(r"[\n\t\s]*", "", sys.stdin.read()) #This line strips all white space and new line chars
print(file)
fileSize = len(file)

def split(str, bitSize): ##The bitsize will determine how long each bit for assic will be
    count = len(str)/bitSize
    returnString = ""
    start = 0
    for x in range(count):
        '''j = str[start:start+bitSize]
        if(int(j,2) == 8):
            print('{} - {}'.format(int(j,2),"BackSpace"))
        elif(int(j,2)==32):
            print('{} - {}'.format(int(j, 2), "Space"))
        else:
            print('{} - {}'.format(int(j, 2), chr(int(j,2))))''' #This code will be for debugging purpose only
        returnString+=chr(int(str[start:start+bitSize],2)) #This is where we generate the actual string
        start += bitSize
    return returnString


if ((fileSize % 7) == 0) and ((fileSize % 8) == 0):
    print(split(file, 7))
    print(split(file, 8))
elif (fileSize % 7) == 0:
    print(split(file, 7))
elif (fileSize % 8) == 0:
    print(split(file, 8))
else:
    print("ERROR")

