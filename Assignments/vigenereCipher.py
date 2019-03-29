import sys
import re

def keyGenerator(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i % len(key)])
    print(key)
    return("".join(key))


def cipherText(string, key):
    for i in range(len(string)):
        if (ord(string[i]) >= 65 and ord(string[i]) < 91):
            x = (ord(string[i])+ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        elif (ord(string[i]) and ord(key[i]) >= 97 and ord(string[i]) and ord(key[i]) < 123):
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('a')
            cipher_text.append(chr(x))

        else:
            cipher_text.append(string[i])

    return ("".join(cipher_text))


def decipherText(cipher_text, key):
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i])-ord(key[i])+26) % 26
        x += ord('A')
        original_text.append(chr(x))
    return("".join(original_text))



cipher_text = []
original_text = []
keyword = (re.sub(r'\s', '', sys.argv[2], count=100))
keyword = keyword.upper()
string = input()


if sys.argv[1] == '-e':
    key = keyGenerator(string, keyword)
    cipher_text = cipherText(string, key)
    print(cipher_text)


elif sys.argv[1] == '-d':
    key = keyGenerator(string, keyword)
    original_text = decipherText(string, key)
    print(original_text)


else:
    print("Program needs -e to encode or -d decode")
    sys.exit()



