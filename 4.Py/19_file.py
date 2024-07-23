import os
import shutil

file_path = "/Users/nikhil/Developer/Practice Codes/4.Py"
folder_path = "/Users/nikhil/Developer/Practice Codes/4.Py/test"

# File detection
if os.path.exists(path=file_path):
    print('File Found')
    if os.path.isfile(path=file_path):
        print("isAFile")
    elif os.path.isdir(folder_path):
        print('isADirectory')
else:
    print('Location does not exists!')

# Read 
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('File Not Found!')

# Write

text = "\nSee you later" 
with open('text.txt', 'a') as file:
    file.write(text)

# Copy
shutil.copyfile('test.txt', 'text.txt')