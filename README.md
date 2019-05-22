# Team-Aztecs
This repository is for Team Aztecs. This will serve as a place for files to help during CyberStorm 

# Binary Decoder
The command to run the Binary Decoder would be: **python BinaryDecoder.py < [Binary text]**  
You can put the binary into a **.txt** file and input it in at the command line or you can put the binary directly into the program.  
 > python BinaryDecoder.py < input.txt

# Vigenere Cipher
The command to run the Vigenere cipher would be: **python VigereCipher.py [-e] [-d] <key>**
Here **-e** means to encrypt and **-d** means to decrypt and **key** means the key that will be used to decipher or encrpyt  
After running the command you will be able to type in the terminal  
After typing and hitting enter, you cipher text or plaintext should apper.  
Alternatly you can input a file at the command line, you will not be able to type after entering input file.  
> python Vigen`ereCipher.py -e MyKeY  
> hello  
> tcvpm

> python Vigen`ereCipher.py -d MyKeY  
> tcvpm  
> hello  

# FTP Covert 
The command to run the covert FTP would be: **python FTP.py**  
Upon running this you should receive your extrated message.  
Getting a certain message does depend on what server and how the files are being hidden.  
> python fetch.py  
> This is my C0V3rt message!  
> Bwahahahahaha!

# Chat Timing 
The command to run the Chat timing program would be: **python Client.py**
Upon running this program you should receive text after receving the program has recevied the text  
The passcode should be present

# Timelock
For this program make sure that the system time is correct ortherwise, you could receive a wrong code.
The command to run the Timelock would be: **python Timelock.py < time.txt**
Here the time.txt is the epoch time that you need in order to get a code.  
The epoch time needs to be in the format of: 'Y m d H M S'  
Y stands for four digit year  
m stands for two digit month  
d stands for two digit day  
H stands hour in miltary time 0-23  
M stands for minutes 0-59  
S stands for second 0-59
**Example Epoch time: 2017 04 26 15 14 30**  
> python Timelock.py < time.txt  
> bc45

# XOR Crypto
For this program make sure in the directory when calling the program you have a file that is named key in your directory.  
You need to make sure the two files are the same as well.  
The command to run XORCrypto would be: **python XORCrypto.py < [input file] > [output file]**  
Input file would be the file you wish to xor, and output file would be the result.
> python XORCrypto.py < test.txt > result.txt

# Steg
The command to run steg would be:  
**python Steg.py [-b][-B] -r -o[offset] -i[interval] -w[wrapper file] > result.txt**
Here you can only one of the methods. The -b: Bit method or -B: Byte method. 
The offset needs to be preset, the interval is the interval between each bit or byte and
the wrapper file is the file that you are extrating from.
When using the -b bit method, the interval does not need to be specified.
> python Steg.py -B -r -o1024 -i8 -w stegged-byte.bmp > timeTest.txt  
> python Steg.py -b -r -o1024 -i8 -w stegged-byte.bmp > timeTest.txt  
> python Steg.py -b -r -o1024 -w stegged-byte.bmp > timeTest.txt  
