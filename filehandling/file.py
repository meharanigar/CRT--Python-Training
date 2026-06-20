'''
Files helps store data permanently

File Handling:
it is a process of 
1.creating files
2.reading the files
3.writing the files
4.updating the files
using python

why file handling?
data disappears after the program


Type of files ???
  text files
1. .txt
2. .csv
3. .py
4. .json

Binary files:
1.images
2.videos
3.pdf's

------------------------------------------------
 Opening the files
syntsx:

 ***file = open("Filename","mode")***
------------------------------------------------
'''
# r--> tell to python that line doesn'thave any escaping charectors
file = open(r"C:\Users\khaza\OneDrive\pyhton2\filehandling\data.txt","r")
print(file)

'''
 File Modes:
--------------------------------------------------------|
mode                 |                 meabning         |
--------------------------------------------------------|
r                    |                 Read             |
w                    |                 Write            |
a                    |                 Append           |
r+                   |                 read and write   |
w+                   |                 write and read   |
a+                   |                 append and read  |
rb                   |                 read binary      |
wb                   |                 write binary     |
---------------------------------------------------------
'''
try:
    file = open(r"C:\Users\khaza\OneDrive\pyhton2\filehandling\data.txt","r")
    data=file.read()
    print(data)
    file.close()
except FileNotFoundError as e:
 print("no file found ")

# Write mode
file = open(r"C:\Users\khaza\OneDrive\pyhton2\filehandling\data.txt","w")
file.write("Hello students")
file.close()
#create file if not exist 
#when we use write mode it 
#delete the previous data and write the new daata in the file
#--------------------------------------------------------------
#append - mode:
#append mode adds the data at end
file = open(r"C:\Users\khaza\OneDrive\pyhton2\filehandling\data.txt","a")
file.write("\nHow are you meher nigar?")
file.close()
#-----------------------------------------------------------------
#create mode - X(Creating a new file only)
file =open("newfile.txt","x")
#gives FileExistsError if the already avaliable
#--------------------------------------------------------

# Read()
'''file = open("newfile.txt","r")
print(file.read())
file.close()'''
#readline()
file = open(r"C:\Users\khaza\OneDrive\pyhton2\filehandling\newfile.txt","r")
print(file.readline())
file.close()

#readlines()-->reads multiple lines
file = open("newfile.txt","r")
lines = file.readlines()
print(lines)
file.close()

#readlines--->converts to list

#write ---> writes the data to file
file = open("newfile.txt","w")
file.write("mehar")
file.write("rahu\n")
file.close()


#writelines():writes list data
'''-------------------------------------------------'''
#pointer methods:
#returns the current cursor position
#tell()
file = open("newfiles.txt",'r')
print(file.tell())
file.read(5)
print(file.tell())
file.close()


#seek():moves the cursor position
file = open("newfile.txt","r")
file.seek(3)
print(file.read())
file.close()

'''-----------------------------------------------'''

#with open()
with open("newfile.txt","r") as file:
   print(file.read())
#automatic closing