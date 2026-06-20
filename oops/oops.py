'''
OOPS: object oriented programming(paradigm)

programs are organized using objects
-----------------------------------
object contains:
1.data(variables)
2.behaviour (functions/methods)
----------------------------------------
oop not only focuses on functions
but also real world entities
car-->object
student-->object
----------------------------------

Each object here:
will have properties and actions
            |              |
            variables      method

------------------------------------


Earlier the programming was written with out oops

1.difficult to manage the large level
2.code duplication
3.less security
4.difficult maintence

OOPS: solve the above problems:
1.classes
2.object
----------------
3.encapsulation
4.inheritance
5.abstraction
6.polymorphism
'''
#procrdural programming
name = "mehar"
marks = 89
def display():
    print(name,marks)
display()


# class=keywork    class name=student

#OOP approch
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name,self.marks)
#object
s1 = Student("mehar",69)
s1.display()
#data+functions--->
'''
advantages:
1.code reusability
2.better organization -- modular and structure
3.security --> encapsulation
4.easy maintenance: to update,debug
5.real world modelling
6.scalability :large application

'''
'''
#class: Blueprint of an object
collection of var, methods

Blueprint:
can be used to build many houses

'''
class M:
    pass
'''
class: keyword creates class
classname: identifiers
pass: emptyblock
'''

#object:instance of a class
# or
#actual memory representation of class 
class Student:
    pass
#create an object
obj = Student()
print(obj)
'''
obj -- > instance name (object)
Student --> class name
'''

class Car:
    brand = "AUdi"
    def start(self):
        print("car started")
#self --> refer current object

#create the  object
#both objects has different memory location
c1 = Car()
c2 = Car()
c1.start()
c2.start()
print(c1.brand)#class--> object for brand inside the class
#
'''
create a class name employee
two variablesn company name and name_employee
create two methods to access name and name_emp
'''
class Employee:
    name = "mehar"
    roll = 23
    def start(self):
        print("class starts")
    def end(self):
        print("class end")
m1 = Employee()
m2 = Employee()
print(m1.name)
print(m2.roll)
m1.start()
m2.start()


class Employee1:
    company_name = "chalapathi"
    def name(self):
        print("vijaya")
e1 = Employee1()
e1.name()
class Employee2:
     employee_name = "mehar" 
     def company(self):
         print("chalapathi")
e2 = Employee2()
e2.company()