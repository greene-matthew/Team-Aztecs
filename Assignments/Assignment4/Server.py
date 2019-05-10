import socket
import time
from binascii import hexlify

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = "Some message...Some message...Some message...Some message...Some message..." 

port = 1337



def sendMes(covert_bin, msg):
    s.bind(("localhost", port))
    ZERO = 0.025
    ONE = 0.1
    s.listen(0)
    n = 0
    c, addr = s.accept()
    for i in msg:
        c.send(i)
        if (covert_bin[n] == "0"):
            time.sleep(ZERO)
        else:
            time.sleep(ONE)
        n = (n + 1) % len(covert_bin)
    c.send("EOF")
    c.close()


covert = "ABC"+"EOF" #This is the message that will be sent covertly
covert_bin = ""
for i in covert:
    covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

print covert_bin
sendMes(covert_bin,msg)
