import os
import binascii

key = open("key2", "rb")
message = open("ciphertext2", "rb")

compare1 = bin(int(binascii.hexlify(message.read()), 16))
compare2 = bin(int(binascii.hexlify(key.read()), 16))
print(len(compare1))
print(len(compare2))
message.seek(0, os.SEEK_END)
print(message.tell())

key.seek(0, os.SEEK_END)
print(key.tell())
sub = len(compare2) - len(compare1)
print sub

print(len(compare2))
binaryString = int(compare1, 2) ^ int(compare2, 2)

real = bin(binaryString)
print len(real)
returnString = int(real, 2)
pic = binascii.unhexlify('%x' % returnString)
print pic

//Hello
