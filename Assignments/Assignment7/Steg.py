import binascii
import sys
import parser
import argparse
import re

import os
import time


sentinel = '00ff0000ff00'
sentinel.decode("hex")


def byteMethodStore(wrapperFile, interval, hiddenFile, offset):
    i = 0
    while i < len(hiddenFile):
        wrapperFile[offset] = hiddenFile[interval]
        offset += interval
        i += 1

    i = 0
    while i < len(sentinel):
        wrapperFile[offset] = sentinel[i]
        offset += interval
        i += 1


def byteMethodRetreive(hexlist, interval, offset, wrapperFileSize):
    i = offset
    resultString = ""
    while i < wrapperFileSize:

        t = hexlist[i]
        resultString += t
        if '00ff0000ff00' in resultString:
            break

        i += interval
    return resultString.decode("hex")





def bitMethodRetreive(wrapperFile, interval, offset, wrapperFileSize):
    i = offset
    returnString = ""

    while i < wrapperFileSize:

        byte = 00000000

        for k in range(8):
            wrapperFile.seek(i, 0)
            read = wrapperFile.read(1)
            wbyte = ord(read)
            bit = wbyte & 00000001
            byte |= bit
            if(k != 7):

                byte = byte << 1
            i += interval

        returnString += chr(byte)
        if( '00ff0000ff00'.decode("hex") in returnString):
            returnString = returnString[:-6]
            break
    return returnString


#wrapperFile = open("stegged-bit.bmp", "rb")
#wrapperFileSize = os.stat("stegged-bit.bmp")
wrapperFile = open("stegged-byte.bmp", "rb",)
wrapperFileSize = os.stat("stegged-byte.bmp")
with open("stegged-byte.bmp", "rb") as f:
    hexdata = binascii.hexlify(f.read())
#hexlist = map(''.join,zip(hexdata[::2],hexdata[1::2]))
#sys.stdout.write(byteMethodRetreive(hexlist, 8, 1024, wrapperFileSize.st_size))

