import time
import hashlib

format = "%Y %m %d %H %M %S"

# epochTime = int(time.time())
epochTimeInput = "1999 12 31 23 59 59"
epochTimeStruct = time.strptime(epochTimeInput, format)

epochTimeSec = epochTimeStruct.tm_sec
epochTime = time.mktime(epochTimeStruct)

systemTimeInput = "2013 05 06 07 43 25"
systemTimeStruct = time.strptime(systemTimeInput, format)
systemTimeSec = systemTimeStruct.tm_sec
systemTime = time.mktime(systemTimeStruct)

timeElapsedInt = int(systemTime) - int(epochTime)

if (systemTimeSec > epochTimeSec):
    timeElapsedInt -= (systemTimeSec - epochTimeSec)
elif (systemTimeSec < epochTimeSec):
    timeElapsedInt -= (60 % epochTimeSec) + systemTimeSec

timeElapsed = str(timeElapsedInt)

firstHash = hashlib.md5(timeElapsed).hexdigest()

hashString = hashlib.md5(firstHash).hexdigest()


def getCode(hashString):
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
    return returnString

print getCode(hashString)

print 60 % 59
