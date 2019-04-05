# Aztecs: Behram Dossabhoy, Matthew Greene, Prasil Mainali, Logan Mccarthy, Joshua Mendoza, Louis Miller, Tracy Samanie
# 5 April 2019
# FTP Covert Channel: use Dr. Gourd's FTP server files and directories as a covert channel

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



# Old code
# Sourced from https://www.pythonforbeginners.com/code-snippets-source-code/how-to-use-ftp-in-python
# Accesses Gourd's FTP server and prints out the files and permissions

''' My old code that wouldn't want to work with me
ftp = FTP('jeangourd.com')
ftp.login()
fileList = []
filePermissions = []
filePermissionsBinary = [];
ftp.retrlines('LIST', fileList.append)

# Store permissions for each file/link/directory in an array
for entry in fileList:
    filePermissions.append(entry[3:10].strip())

##    if (len(filePermissions) % 7 == 0):
for element in range(len(filePermissions)):
    for character in element:
        if (character != '-'):
            filePermissionsBinary.append(1)
        else:
            filePermissionsBinary.append(0)
                    
# Print the filePermissions array
print(filePermissions)
print(filePermissionsBinary)
'''
