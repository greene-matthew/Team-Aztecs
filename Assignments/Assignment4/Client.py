# Aztecs: Behram Dossabhoy, Matthew Greene, Prasil Mainali, Logan Mccarthy, Joshua Mendoza, Louis Miller, Tracy Samanie

import socket
import sys
from time import time

ONE = 0.25
Bits = 8


def convertToAscci(binaryString):
    num = int(binaryString, 2)
    return chr(num)


def convertTimesToBinary(times):
    convert_bin = ""

    for i in times:
        print(i)
        if (i >= ONE):
            convert_bin += "0"
        else:
            convert_bin += "1"
    return convert_bin


def binaryToAscci(convert_bin):
    count = 0
    message = ""

    while count <= len(convert_bin):
        message += convertToAscci(convert_bin[count:count + Bits])
        count += Bits

    return message





def main():
    # This code below gets us connected to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.jeangourd.com", 31337))
    print("CONNECTED")

    #This code will take the time between each char and put it into an array
    times = []
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    while (data.rstrip("\n") != "EOF"):
        times.append(round(t1 - t0, 3))
        sys.stdout.write((data))
        sys.stdout.flush()
        t0 = time()
        data = s.recv(4096)
        t1 = time()

    s.close()

    # Below is an array of the times bewteen each char
    print(times)

    print(binaryToAscci(convertTimesToBinary(times)))


main()
