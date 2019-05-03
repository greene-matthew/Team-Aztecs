import binascii
import math
import sys
import argparse
import os

sentinel = '00ff0000ff00'
sentinelHex = binascii.hexlify(sentinel)
sentinelHex = map(''.join, zip(sentinelHex[::2], sentinelHex[1::2]))


def byteMethodStore(wrapperFileHex, interval, hiddenFileHex, offset):
    o = offset
    i = 0
    while i < len(hiddenFileHex):
        wrapperFileHex[o] = hiddenFileHex[i]
        o += interval
        i += 1

    i = 0
    while i < len(sentinelHex):
        wrapperFileHex[o] = sentinelHex[i]
        o += interval
        i += 1

    return "".join(wrapperFileHex).decode("hex")


def bitMethodStore(wrapperFileHex, interval, hiddenFileHex, offset):
    i = offset
    j = 0
    returnString = ""

    while j < len(hiddenFileHex):
        hByte = int(hiddenFileHex[j], 16)
        for k in range(8):
            wByte = int(wrapperFileHex[i], 16)
            wByte &= 11111110
            wByte |= ((hByte & 10000000) >> 7)
            wrapperFileHex[i] = binascii.hexlify('%x' % wByte)
            if (k != 7):
                hByte = hByte << 1
            i += interval
        j += 1

    n = 0
    while n < len(sentinelHex):
        sByte = int(sentinelHex[n], 16)
        for k in range(8):
            wByte = int(wrapperFileHex[i], 16)
            wByte &= 11111110
            wByte |= ((sByte & 10000000) >> 7)
            wrapperFileHex[i] = binascii.hexlify('%x' % wByte)
            if (k != 7):
                sByte = sByte << 1
            i += interval
        n += 1

    returnString += "".join(wrapperFileHex)
    return returnString.decode("hex")


def byteMethodRetreive(wrapperFileHex, interval, offset):
    returnString = ""

    i = offset
    while i < len(wrapperFileHex):
        t = wrapperFileHex[i]
        returnString += t
        if sentinel in returnString:
            returnString = returnString[:-6]
            break

        i += interval
    return returnString.decode("hex")


def bitMethodRetreive(wrapperFileHex, interval, offset):
    i = offset
    returnString = ""

    while i < len(wrapperFileHex):
        byte = 00000000
        for k in range(8):
            wByte = int(wrapperFileHex[i], 16)
            bit = wByte & 00000001
            byte |= bit
            if (k != 7):
                byte = byte << 1
            i += interval

        returnString += chr(byte)
        if (sentinel.decode("hex") in returnString):
            returnString = returnString[:-6]
            break

    return returnString


parser = argparse.ArgumentParser(description="Arguments for Steg", add_help=False)
parser.add_argument('-b', '--bit', default=False, action='store_true')
parser.add_argument('-B', '--byte', default=False, action='store_true')
parser.add_argument('-s', '--store', default=False, action='store_true')
parser.add_argument('-r', '--retrieve', default=False, action='store_true')
parser.add_argument('-o', '--offset', type=int)
parser.add_argument('-i', '--interval', type=int)
parser.add_argument('-w', '--wrapperFile', type=str)
parser.add_argument('-h', '--hiddenFile', type=str)
args = parser.parse_args()


def main():
    if (args.bit == False and args.byte == False) or (args.bit == True and args.byte == True):
        print("please choose either the byte or bit method")
        sys.exit()
    elif (args.store == False and args.retrieve == False) or (args.store == True and args.retrieve == True):
        print("please choose to either store or retrieve a hidden file")
        sys.exit()
    elif (args.offset == None):
        print("Please specify an offset")
        sys.exit()
    elif (args.wrapperFile == None):
        print("Specify a Wrapper File")
        sys.exit()
    elif (args.store == True and args.hiddenFile == None):
        print("In order to store, specify a file to hide")
        sys.exit()
    
    wrapperFileHex = binascii.hexlify(open(args.wrapperFile,"rb").read())
    wrapperFileHex = map(''.join, zip(wrapperFileHex[::2], wrapperFileHex[1::2]))

    if args.bit == True and args.store == True:
        hiddenFileHex = binascii.hexlify(open(args.hiddenFile, "rb").read())
        hiddenFileHex = map(''.join, zip(hiddenFileHex[::2], hiddenFileHex[1::2]))
        if (args.interval == None):
            interval = 1
        else:
            interval = args.interval
        return (bitMethodStore(wrapperFileHex, interval, hiddenFileHex, args.offset))

    if args.bit == True and args.retrieve == True:
        if (args.interval == None):
            interval = 1
        else:
            interval = args.interval
        return (bitMethodRetreive(wrapperFileHex, interval, args.offset))

    if args.byte == True and args.store == True:
        hiddenFileHex = binascii.hexlify(open(args.hiddenFile, "rb").read())
        hiddenFileHex = map(''.join, zip(hiddenFileHex[::2], hiddenFileHex[1::2]))
        if (args.interval == None):
            interval = math.floor((len(wrapperFileHex) - args.offset) / (len(hiddenFileHex) + 6))
        else:
            interval = args.interval
        return (byteMethodStore(wrapperFileHex, interval, hiddenFileHex, args.offset))

    if args.byte == True and args.retrieve == True:
        return (byteMethodRetreive(wrapperFileHex, args.interval, args.offset))


# wrapperFile = open("stegged-bit.bmp", "rb")
# wrapperFileSize = os.stat("stegged-bit.bmp")
print main()
# hexlist = map(''.join,zip(hexdata[::2],hexdata[1::2]))
# sys.stdout.write(byteMethodRetreive(hexlist, 8, 1024, wrapperFileSize.st_size))
