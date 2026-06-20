'''
CSV -->Common Separate Values
used: excel,reports,databases

namw,age.branch
mehar,20,ds
nigar,21,cs
'''
import csv
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["mehar","20","CAI"])
    writer.writerow(["nigar","19","CSE"])
    writer.writerow(["kavya","22","AIML"])

#Read CSV
#data will be read in list format
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Binary file handling
# file = open(r"C:\Users\khaza\OneDrive\pyhton2\filehandling\WhatsApp Image 2024-12-13 at 2.47.35 PM copy.jpeg","rb")
# data = file.read()
# print(data)

#task 1: count words in a file
with open("data.txt","r") as file:
    content = file.read()
    words = len(content.split())
    print(words)

#task2:
with open("data.txt","r") as file:
    content = file.read()
    words = len(content.splitlines())
    print(words)

#task3:search a word in a file
ch = input("enter the ch:")
with open("data.txt","r") as file:
    content = file.read()
    if ch in content:
        print("word found")
    else:
        print("no word")
    
#task 4: copy one file to another file
# with open("data.txt", "r") as f1:
#     content = f1.read()
# with open("copy.txt", "w") as f2:
#         f2.write


with open("data.txt","r") as file:
    content = file.write()
    print(content)

'''
1.accept student_name and marks
2.store records in a file
named students.txt
3.display all records
4.handle file exceptions 

'''
class StudentManager:
    def add_student(self):
        try:
            name = input("Nmae:")
            marks = input("marks:")
            with open("students.txt","a") as file:
                file.write(name + " " + marks)
            print("records adden")
        except Exception as e:
            print(e)
        def display_records(self):
            try:
                with open("students.txt","r") as file:
                    content = file.read()
                    print("student records:")
                    print(content)
            except FileNotFoundError as e:
                print(e)
obj = StudentManager()
obj.add_student()
obj.display_records



