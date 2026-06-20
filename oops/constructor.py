'''
constructor : __init__()
special method
automatically called when object is create


used: initializing  the object data

'''
class Student:
    def __init__(self):
        print("constructor is called")
s1 = Student()

#===========================================
'''
student()
|
object created
|
__init__ automatically called

----------------------------------

if no constructor :
manually assing the values
if yes
automatically initialization
'''
class Student:
    pass
s1 = Student()
s1.name = "mehar"
s1.branch = "AI"

#example with constructor
class Student:                        #self refer to the current object(object)
    def __init__(self):
        self.name = "mehar"
        self.age = 20
object = Student()
print(object.name)
print(object.age)

#constructor with parameters
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj2 = Student("mehar",19)
print(obj2.name)
print(obj2.age)        
'''
self --> obj2
name:"mehar"
age : 19

obj2_______
name = "mehar"
age = 19
'''
'''
----------------------------------|
|  step by step:                  |
----------------------------------|
1.object memory allocated         |
2.__init__ is called automatically|
3.self points to object           |
4.variables initialized           |
5.object returned                 |
-----------------------------------
'''
''''
default constructor

class Test:
    def __init__(self):
        print("default constructor")
t = Test()

#parametrized constructor
class Test:
    def __init__(self,name,age):
        print("parametrized constructor")
t = Test()
'''
'''
----------------------------------------------------------------
constructor                    |            Normal method
------------------------------------------------------------------
automatically called           |          manually call it 
name fixed: __init___          |          any name
used for intialization         |       used for operations
executes during object         |        executess when called
-----------------------------------------------------------------
'''

class Student:
    def __init__(self):
        print("constructor")
    #normal method
    def display(self):
        print("normal method")
c1 = Student()

'''
 Istance Variables:

 variables that belong to an object
 separate copy created  for every object

They store:
 object -- specific data

Student | Name     | Marks
s1       vijaya      98
s2       rajesh      99
 
 each object store it's own data

'''
class Student:
    def __init__(self,name,marks):
        #instance variables
        self.name = name
        self.marks = marks
s1 = Student("mahar",98)
s2 = Student("rajesh",99)
print(s1.name,s1.marks)

#object do not sahre instance variable
'''
instance variable:

'''
#instance variable
class Student:
    def __init__(self,name,marks):
        #instance variables
        self.name = name
        self.marks = marks
    #instance method
    def display(self):
        print(self.name)
        print(self.marks)
s1 = Student("rajesh",98)
s1.display()

'''
------------------------------------
flow of the instance methods:
s1.display()
|
Student.display(self)
|
self---->s1
---------------------------------------
'''

'''
Dynamic object properties
adding the variables dynamically

After creating the object
'''
class Student:
    pass
s1 = Student()
s1.name = "nigar"
s1.age = 19
print(s1.name,s1.age)

'''
class variables:
class variable shared all among the object

'''
class Student:
    #class variable
    college_name = "city"
    def __init__(self,branch):
        #instance variable
        self.branch = branch

        #normal method 
    def display(self):
        print(self.college_name)
s1 = Student("ai")
s2 = Student("csd")
print(s1.college_name)


'''
self: self refer to current object
             or
reference variable pointig to current object

'''
class Student:
    def display(self):
        print("hello")
s1 = Student()
s1.display()
'''
s1.display()
|
student.display(s1)
|
self -s1(self points to s1)
'''
class Student:
    def show(self):
        print(self)
s1 = Student()
print(s1)
s1.show()
'''
    student class
    -------------
    college = city  # stored in class memory
    -------------
    |       |
    s1      s2
class employee:
    company = "google"
    def display(self):
        self.company = company
        print(self.company)
e = employee()
two ways access:
print(e.company)

-----------------------------
#no object use
print(employee.company)
'''

#Task : create a class named as employee 
# create one class variable
# use @classmethod to apply
# on method company_name
#print the company name
#using multiple objects

class Employee():
    var_name = "mehar"
    @classmethod
    def company_name(cls):
        print(cls.var_name)
s1 = Employee()
s1.company_name()
s2 = Employee()
s2.company_name()

class Employee():
    var_name = "mehar"
    @classmethod
    def company_name(cls,new_name):
        cls.var_name = new_name

Employee.company_name("google")
print(Employee.var_name)

       
'''
difference between instance method and class method
--------------------------------------------------------------------
instance method             |         class method
---------------------------------------------------------------------
worksn on the object data   |          works on class data
uses self                   |          uses cls
need object                 |          directly use class
access the intance variable |          access class variables
----------------------------------------------------------------------
'''
#Example:write a code by using the both instance and class method:

#instance method:refer object
def instance_method(self):
    print("instance method")

#class method : refers class
@classmethod
def class_method(cls):
    print("class method")

'''
Static Method:
does not uses : object,class

They Are:
utility/helper methods

Not uses:
slef,cls -- >

decorator :
@staticmethod 


'''
#static method example:
class Calculator:
    @staticmethod  #helper method
    def add(a,b):
        return a+b
print(Calculator.add(10,20))

#independent method
#logically belongs to class but no data required from the class
class Message:
    @staticmethod
    def greet():
        print("hello Students")
print(Message.greet())


#Task: create a class named as student 
#create constructor
#class variables
#instance variable
#instance methods
#class method
#static method
class Student:
    name = "mehar"
    def __init__(self,marks,roll,branch):
        self.marks = marks
        self.roll = roll
        self.branch =branch
    def display(self):
         print("Name:", Student.name)
         print("Marks:", self.marks)
         print("roll:", self.roll)
         print("Branch:", self.branch)

    @classmethod
    def class_method(cls,new_name):
        cls.name = new_name
    @staticmethod
    def welcome():
        print("hello")
Student.welcome()
Student.class_method("nigar")
s1 = Student(95,1,"CAI")

s1.display()




        
    