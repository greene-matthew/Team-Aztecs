# Aztecs: Behram Dossabhoy, Matthew Greene, Prasil Mainali, Logan Mccarthy, Joshua Mendoza, Louis Miller, Tracy Samanie

import socket
import sys
from time import time
from binascii import unhexlify

ONE = 0.07
Bits = 8


def convertToAscci(covert_bin):
	covert = ""
	i = 0
	while (i < len(covert_bin)):
	# process one byte at a time
		b = covert_bin[i:i + 8]
	# convert it to ASCII
		n = int("0b{}".format(b), 2)
		try:
			covert += unhexlify("{0:x}".format(n))
		except TypeError:
			covert += '?'
	# stop at the string "EOF"
		i += 8


def convertTimesToBinary(times):
	convert_bin = ""

	for i in times:
		#print(i)
		if (i >= ONE):
			convert_bin += "1"
		else:
			convert_bin += "0"
	print convert_bin
	return convert_bin


def binaryToAscci(covert_bin):
	covert = ""
	i = 0
	while (i < len(covert_bin)):
		# process one byte at a time
		b = covert_bin[i:i + 8]
		# convert it to ASCII
		n = int("0b{}".format(b), 2)
		try:
			covert += unhexlify("{0:x}".format(n))
		except TypeError:
			covert += "?"
		# stop at the string "EOF"
		i += 8
		if 'EOF' in covert:
			break
	return covert[:-3]


def main():
	# This code below gets us connected to the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("www.jeangourd.com", 31337))
	print("CONNECTED")

	#This code will take the time between each char and put it into an array
	times = []

	data = s.recv(4096)

	while (data.rstrip("\n") != "EOF"):

		sys.stdout.write((data))
		sys.stdout.flush()
		t0 = time()
		data = s.recv(4096)
		t1 = time()
		times.append(round(t1 - t0, 3))
	s.close()

	# Below is an array of the times bewteen each char
	#print(times)

	print(binaryToAscci(convertTimesToBinary(times)))


main()
