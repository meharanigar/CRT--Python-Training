'''
Abstraction?
what is abstraction?
Hiding the internal implementation details 
showing the essential features to the user
                or
        what operation is done?
        but not:
        how operation is working internally 
---> complexity is hidden from the user
why we use abstraction?
1. reduces the complexiy
2. improves the security 
3. better maintance
4. cleaner code
5. standardization

#abstraction in python
python supports abs using:
abstract classes
abstract methods

# ABC module
ABC --> abstract base class

ABstract class
blueprint of a class
cannot create objects directly

# defines basic common structure 
abstract can have:
1.abs methods
2. normal method

#abstract method
methods declared but:
    implementation not provided
child class must implement it
ex:
vehicle
-> start()

#ABC --> absstract base class

#abstract class
from abc import ABC,abstractmethod
class Vehicle(ABC):
    #abstract method
    @abstractmethod
    def start(self):
        pass






'''
#abstract class
from abc import ABC,abstractmethod
class Vehicle(ABC):
    #abstract method
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car started")
        
c1 = Car()
c1.start()

#example2:
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("dog barks")
d1 = Dog()
d1.sound()

#example3
#multiple abstract methods 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Area formula")
    def perimeter(self):
        print("perimeter formula")
r1 = Rectangle()
r1.area()
r1.perimeter()

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    #normal method
    def sleep(self):
        print("sleeping")
class Dog(Animal):
    def sound(self):
        print("bark")
d2 = Dog()
d2.sound()
d2.sleep()

#payment system:
#pay()
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass
class Phonepay(PaymentGateway):
    def pay(self):
        print("paid using phonepay")
class Paytm(PaymentGateway):
    def pay (self):
        print("paid using paytm")
pp = Phonepay()
pt = Paytm()
pp.pay()
pt.pay()
#task: create an abstract clas paymentgateway with two abstrat methods pay and refund
# but amount--: parameter
#now create a child class implementation 
#1 creditcard pay 2. UPI pay
class Paymentgateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
class Creditcardpay(PaymentGateway):
    def pay(self,amount):
        print(f"pay {amount} using creditcard")
    def refund(self,amount):
        print(f"refunded {amount} using creditcard")
class Upipay(PaymentGateway):
    def pay(self,amount):
        print(f"pay {amount} using upi")
    def refund(self,amount):
        print(f"refunded {amount} using upi")
c1 = Creditcardpay()
c1 = Upipay()
c1.pay(50000)
c1.refund(6000)

#task create an abstract class employee
# with abs methods:
#calculate_salary
#create: fulltime employee and parttimeemployee
# rules : fully timesalary = 50000
# parttime salary = hours*500

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FulltimeEmployee(Employee):
    def calculate_salary(self):
        return 50000
class ParttimeEmployee(Employee):
    def __init__(self,hour):
        self.hour = hour
    def calculate_salary(self):
        return self.hour*500        
c1 = FulltimeEmployee()
c2 = ParttimeEmployee(40)
print(c1.calculate_salary())
print(c2.calculate_salary())

'''
food delivery system
create an abstract class resturant
with methods:
1. prepare_food()
2. delivery_time()
create a child classes:
1. pizzashop
2. burger shop
display:
food preparation message 
delivery time
'''

class Restaurant(ABC):
    @abstractmethod
    def prepare_food(self):
        pass
    def delivery_time(self):
        pass
class Pizzashop(Restaurant):
    def prepare_food(self):
        print("food is prepared in our pizzashop")
    def delivery_time(self):
        print("delivery is done in time")
class Burgershop(Restaurant):
    def prepare_food(self):
        print("food is prepared in our burgershop")
    def delivery_time(self):
        print("delivery is done")
c1 = Pizzashop()
c2 = Burgershop()
c1.prepare_food()
c2.delivery_time()
'''
ride booking applications
class -> ride
method:
calculate_fare(distance)
child:
1.bikeride
2.carride
3.autoride
rules: 
bike---> distance*10
car --> distance*20
auto --> *15
'''
'''
class Ride(ABC):
    @abstractmethod
    def calculate_fare(self,distance):
        pass
class bikeride(Ride):
    def calculate_fare(self,distance):
        return distance*10
class carride(Ride):
    def calculate_fare(self,distance):
        return distance*20
class autoride(Ride):
    def calculate_fare(self,distance):
        return distance*15
c1 = bikeride(50)
print(c1.calculate_fare())
c2 = carride(45)
print(c2.calculate_fare())
c3 = autoride(32)
print(c3.calculate_fare())
'''    
'''
Magic methods /dunder methods
__double underscores
dunder --> DOUBLE UNDERSCORES
ex:
    __init__
    ___add__
    why?
operator overloading
+
-
/
print(10+10)#20
print("Hello"+"wprld") #helloworld

class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print(n1+n2)
#make your objects work like buit in types
'''
#__str__
class Student:
    def __str__(self):
        return "Student object"
s1 = Student()
print(s1)

#len() method
class Team:
    def __len__(self):
        return 5
t1 = Team()
print(len(t1))

#== __eq__
'''
class Students:
    def __init__(self,marks):
        self.marks = marks
    def __eq__(self, value):
        return self.marks == value.marks
s1 = Student(90)
s2 = Student(90)
print(s1 == s2)
'''
# repr --> official object representation
# debugging
#development
class Student:
    def __repr__(self):
        return "hello"
s1 = Student()
print(repr(s1))