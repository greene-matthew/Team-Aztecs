# Aztecs
# Behram Dossabhoy, Matthew Greene, Prasil Mainali, Logan Mccarthy, Joshua Mendoza, Louis Miller, Tracy Samanie
# 30 April 2019
# XOR Crypto
# Github: https://github.com/greene-matthew/Team-Aztecs


import binascii
import os
import sys

if(sys.platform == 'win32'): ##This is so if this program is run on windos in gives the stdin in binary
    import msvcrt

    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)


key = open("file2", "rb")
keyLength = len(open("file2", "rb").read())

message = sys.stdin ##
message.seek(0,2)
messageLength = message.tell()
message.seek(0,0)



#print (keyLength)
#print (messageLength)

if (keyLength > messageLength): ##This if statment will handle if the key is larger then the message
    bytesToRead = keyLength - (keyLength - messageLength) ##We get the number if bytes we actually need and read to
    messageBinary = bin(int(binascii.hexlify(message.read(bytesToRead)), 16))  #that number
    keyBinary = bin(int(binascii.hexlify(key.read(bytesToRead)), 16))
elif (messageLength > keyLength):           ## This if statment handles if the message is larger then the key
    extraBytes = messageLength - keyLength  ##if so we will go back to the start of the file and read the bytes so they are even
    messageBinary = bin(int(binascii.hexlify(message.read(messageLength)), 16))
    keyBinary = bin(int(binascii.hexlify(key.read()), 16))
    key.seek(0, 0)
    keyBinary += bin(int(binascii.hexlify(key.read(extraBytes)), 16))[2:]
else:
    messageBinary = bin(int(binascii.hexlify(message.read(messageLength)), 16))
    keyBinary = bin(int(binascii.hexlify(key.read()), 16))

binaryString = int(messageBinary[2:], 2) ^ int(keyBinary[2:], 2) ##We xor the message and key
returnString = int(bin(binaryString), 2) ##Here we turn binary into a very large numeber
##print(returnString)
print(binascii.unhexlify('%x' % returnString)) ##We turn that binary into ascii
