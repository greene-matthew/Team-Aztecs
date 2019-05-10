import sys
import time
import hashlib
from datetime import datetime

format = "%Y %m %d %H %M %S"


def getSystemTime():
    #systemTimeInput = "2017 04 26 15 14 30"
    #now = datetime.now()
    
    systemTimeInput = datetime.now().strftime(format)
    systemTimeStruct = time.strptime(systemTimeInput, format)
    return systemTimeStruct


def getCode(timeElapsed):
    firstHash = hashlib.md5(timeElapsed).hexdigest()
    hashString = hashlib.md5(firstHash).hexdigest()
    returnString = ""
    alphaCount = 0
    numCount = 0

    for c in hashString:
        if c.isalpha():
            returnString += c
            alphaCount += 1
            if alphaCount == 2:
                break

    for h in reversed(hashString):
        if h.isdigit():
            returnString += h
            numCount += 1
            if numCount == 2:
                break
	length = len(hashString)	
    return returnString + hashString[length/2]


# epochTime = int(time.time())
epochTimeInput = sys.stdin.read().replace('"', '').strip()
epochTimeStruct = time.strptime(epochTimeInput, format)
epochTimeSec = epochTimeStruct.tm_sec
epochTime = time.mktime(epochTimeStruct)

systemTimeStruct = getSystemTime()
timeElapsed = int(time.mktime(systemTimeStruct)) - int(epochTime)

if systemTimeStruct.tm_sec > epochTimeSec:
    timeElapsed -= (systemTimeStruct.tm_sec - epochTimeSec)
elif systemTimeStruct.tm_sec < epochTimeSec:
    timeElapsed -= (60 % epochTimeSec) + systemTimeStruct.tm_sec

print getCode(str(timeElapsed))
