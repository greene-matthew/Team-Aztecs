# Aztecs
# Behram Dossabhoy, Matthew Greene, Prasil Mainali, Logan Mccarthy, Joshua Mendoza, Louis Miller, Tracy Samanie
# 29 March 2019
# Binary Decoder: Decode a string of binary, either in base-7 or base-8
# Github: https://github.com/greene-matthew/Team-Aztecs


import sys
import parser
import argparse
import re



def upperOrLower(char):
    if(char.isupper()):
        return ord(char)-65
    else:
        return ord(char)-97

def getChar(char, plainValue, keyValue):

    if(not args.encode == None):
        returnString = (plainValue + keyValue) % 26
    else:
        returnString = (plainValue - keyValue) % 26

    returnString+=97
    returnString = chr(returnString)
    if(char.isupper()):
        return returnString.upper()
    else:
        return returnString.lower()





def encodeOrDecode(str,encodeKey,decodeKey):
    if(not args.encode == None):
        key = re.sub(r"[\n\t\s]*", "", encodeKey)
    else:
        key = re.sub(r"[\n\t\s]*", "", decodeKey)


    keyCount =0
    returnString = ""
    for char in str:
        if(not char.isalpha()):
            returnString += char
            continue
        else:
            if keyCount > len(key)-1:
                plainTextValue = upperOrLower(char)

                keyCount = 0

                keyTextValue = upperOrLower(key[keyCount])

                returnString += getChar(char,plainTextValue,keyTextValue)


            else:
                plainTextValue = upperOrLower(char)
                keyTextValue = upperOrLower(key[keyCount])
                returnString += getChar(char, plainTextValue,keyTextValue)

        keyCount+=1
    return returnString







parser = argparse.ArgumentParser(description="Encode or decode")
parser.add_argument('-e', '--encode', help="The key to use to encode a message")
parser.add_argument('-d', '--decode', help="The key to use to decode a message")

args = parser.parse_args()

if(args.encode == None and args.decode == None):
    print("Please provide a key to decode or encode")
    sys.exit()

while True:
    input = sys.stdin.readline()
    if not (input == ''):
        print(encodeOrDecode(input,args.encode,args.decode))
    else:
        sys.exit()
