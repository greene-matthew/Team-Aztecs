import ftplib

METHOD = 7
BITS = 7
lines = []


def convertToAscci(binaryString):
    num = int(binaryString, 2)
    return chr(num)


def permissionsToBinary(permissionString):
    binaryString = ""
    for i in permissionString:
        if i == '-':
            binaryString += "0"
        else:
            binaryString += "1"
    return binaryString

#server = ftplib.FTP()
#server.connect(host,port)
#server.login(username,password)
server = ftplib.FTP('www.jeangourd.com', 'anonymous', '')
#Change the value if you need to change directory
#server.cwd('7')
server.retrlines('LIST ', lines.append)
server.quit()
numOfFiles = len(lines)
for i in range(numOfFiles):
    temp = lines[i]
    lines[i] = temp[0:10]

returnString = ""

if METHOD == 7:
    for i in lines:
        if (i[0] != 'd' and i[1] != 'r' and i[2] != 'w'):
            returnString += convertToAscci(permissionsToBinary(i[-METHOD:]))
elif METHOD == 10:
    temp = ""
    for i in lines:
        temp += permissionsToBinary(i[-METHOD:])

    count = 0
    while count <= len(temp):
        returnString += convertToAscci(temp[count:count + BITS])
        count += BITS




#This method is to loop through all possibiltes of the permissions length commented out for non use
'''else:
    checkString = "----------"
    temp = ""
    for i in range(1,10):
        print(i)
        returnString = ""
        METHOD = i
        var = 10 - METHOD
        for i in lines:
            if (checkString[0:var] == i[0:var]):
                temp += permissionsToBinary(i[-METHOD:])
                count = 0
                while count <= len(temp):
                    returnString += convertToAscci(temp[count:count + BITS])
                    count += BITS
        print(returnString)
    exit(0)'''

print(returnString)
