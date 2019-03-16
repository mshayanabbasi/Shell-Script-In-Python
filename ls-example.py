
# reference: how to read directory in python. split string in python
#ls
#echo

import subprocess

while True:
	cmd = raw_input("Shell Script: ")
	cmdList = cmd.split()
	if cmd == 'ls':
		proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
		output = proc.stdout.read()
		print(output)
	elif cmdList[0] == 'echo':
		for output in cmdList:
			if output != "echo":
				print(output)
	elif cmdList[0] == 'cat':
		for file in cmdList: 
			if file != "cat":
				infile = open(file)
				contents = infile.read()
				print(contents)
	else:
		print("Invalid Operators")

