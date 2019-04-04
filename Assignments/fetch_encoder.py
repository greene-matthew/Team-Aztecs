import sys
import re
import os

#sys.stdin.read()


file = re.sub(r"[\n\t\s]*", "", sys.stdin.read()) 

if (file == 'Gen_message'):
	j=1
	message = raw_input('What message would you like to encrypt? ')
	for l in message:
		binary = format(ord(l), '09b')
		print(l, ' = ', ord(l), ' = ', binary)
		i = 0
		string = ''
		for b in binary:
			if (i%3 == 0):
				#print(binary[i+0:i+3])
				#print(int(binary[i+0:i+3], 2))
				string += str(int(binary[i+0:i+3], 2))
			#else if (binary.length - i < 3):				
			i+=1
		print string
		
		# Generate the random files, sort them, and apply the permissions in sorted order
		filename = 'file' + str(j) + '.txt'
		j+=1
		#touch filename
		if not os.path.exists(os.path.dirname(os.getcwd())):
			os.mknod(filename)
		os.chmod(filename, int(string))
		#chmod string filename
		
		i=0
		
		
		