import sys

decode=False
encode=False
key = ''

for arg in sys.argv:
	#checks for decode flag
	if(arg == '-d'):
		decode = True
		
	#checks encode flag
	elif(arg == '-e'):
		encode = True
	
	#anything else thats not the program name becomes the key
	elif not (arg == sys.argv[0]):
		key = arg.lower()
	
length = len(key)
key = key.replace(' ', '') #replaces space with nothing
print(key)

#exit program if flags were not set
if not encode or decode:
	print("Put -d or -e then key to use")
	sys.exit(0)

#exit program if key was not given
if key == '':
	print("Please enter a key")
	sys.exit(0)

while(1):
	out = ''
	index = 0
	text = input()
	
	if encode:
		for i in text:
			if(index == length):
				index = 0 #reset index after the last letter of the key was used

			if i.islower():
				out += (chr((ord(key[index])-97+ord(i)-97)%26+97)) #converts characters to the correct value between 0-25, adds them, and converts the back to ascii
			elif i.isupper():
				out += (chr((ord(key[index])-97+ord(i)-65)%26+65)) #converts characters to the correct value between 0-25, adds them, and converts the back to ascii
			else:
				out += i
				continue #pass non letters staight to output and go to next loop
			index += 1
		print(out)
	
	elif decode:
		for i in text:
			if(index == length):
				index = 0 #reset index after the last letter of the key was used

			if i.islower():
				out += (chr((26-(ord(key[index])-97)+(ord(i)-97))%26+97)) #converts characters to the correct value between 0-25, subtracts key from text, and converts the back to ascii
			elif i.isupper():
				out += (chr((26-(ord(key[index])-97)+(ord(i)-65))%26+65)) #converts characters to the correct value between 0-25, subtracts key from text, and converts the back to ascii
			else:
				out += i
				continue #pass non letters staight to output and go to next loop
				
			index += 1
		print(out)