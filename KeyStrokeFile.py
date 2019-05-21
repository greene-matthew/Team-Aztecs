from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

password = raw_input().strip('[]')
timings = raw_input().strip('[]')
#print password
#print timings
password = password.split(",")
password = password[:len(password) / 2 +1]
password = "".join(password)


timings = timings.split(",")

timings = [float(a.replace('\'',""))-0.003 for a in timings]
keypress = timings[:len(timings)/2 +1]
keyinterval = timings[len(timings)/2 +1:]
keyboard = Controller()


string = "This is supposed to be a fake string"
i = 0
sleep(2)

for char in password.replace('\'',"").replace(' ', ""):
    
    keyboard.press(char)
    sleep(keypress[i])
    
    keyboard.release(char)
    if(i == len(keypress)-1): break
    sleep(keyinterval[i])
    i = i+1
#print "keypress times = {}".format(keypress)
#print "key intervals = {}".format(keyinterval)

tcflush(stdout, TCIFLUSH)

