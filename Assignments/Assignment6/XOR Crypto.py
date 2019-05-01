import binascii

key = open("key2", "rb")
message = open("ciphertext2", "rb")

keyLength = len(open("key2", "rb").read())
messageLength = len(open("ciphertext2", "rb").read())

#print (keyLength)
#print (messageLength)

if (keyLength > messageLength): ##This if statment will handle if the key is larger then the message
    bytesToRead = keyLength - (keyLength - messageLength) ##We get the number if bytes we actually need and read to
    messageBinary = bin(int(binascii.hexlify(message.read(bytesToRead)), 16))  #that number
    keyBinary = bin(int(binascii.hexlify(key.read(bytesToRead)), 16))
elif (messageLength > keyLength):           ## This if statment handles if the message is larger then the key
    extraBytes = messageLength - keyLength  ##if so we will go back to the start of the file and read the bytes so they are even
    messageBinary = bin(int(binascii.hexlify(message.read()), 16))
    keyBinary = bin(int(binascii.hexlify(key.read()), 16))
    key.seek(0, 0)
    keyBinary += bin(int(binascii.hexlify(key.read(extraBytes)), 16))[2:]
else:
    messageBinary = bin(int(binascii.hexlify(message.read()), 16))
    keyBinary = bin(int(binascii.hexlify(key.read()), 16))

binaryString = int(messageBinary[2:], 2) ^ int(keyBinary[2:], 2) ##We xor the message and key
returnString = int(bin(binaryString), 2) ##Here we turn binary into a very large numeber
##print(returnString)
print(binascii.unhexlify('%x' % returnString)) ##We turn that binary into ascii
