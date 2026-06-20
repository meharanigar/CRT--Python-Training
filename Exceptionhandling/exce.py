'''
Error: An error is a problem in the program in
the program causing abnormal termination
---------------------------------------------------

1.syntax error
2.run time eerors--can be handled by the exception
  ---> Occurs while executing the program

  example:
  a = 10
  b = 0
  c = a\b--->zerodivision error

3.Logical errors:
program runs but gives wrong output
example:

3. Logical Errors:
program runs but gives wrong output
Ex: print(2*(3+5)) --->output(16)

-------------------------------------
whitout exception:
1.program crashes
2.poor user experince
3.data loss possible

whit exception:
1.program will execute normally
2.proper error msg
3.safer application

----------------------------------------
#basic exception handling:
syntax:
ketwords: try , catch, finally, raise




'''
#lets write our first program
try:
    num = int(input("enter the num:"))
    print(10/num)
except:
    print("some error occured")

#Risky code will be inside try
#if exception occurs -->exception

#above is not a good practice
#hides actual problem
#difficult to drbug
try:
    num = int(input("enter the num:"))
    print(10/num)
except ZeroDivisionError:
    print("cannot divide with 0")
except ValueError:
    print("input should not be string")

'''
-------------------------------------------
Common python exceptions:                 |
1.ZeroDivisionError ---> divide with zero |
2.VlaueErroe --> invalid input            |
3.TypeError ---> wrong datatype           |
4.IndexError --> invalid index            |
5.KeyError --->  invalid dictionary key   |
6.FileNotFoundError --> invalid attributes| 
7.AttributeError --> invalid attribute    |
8.NameError --> variable is not defined   |
-------------------------------------------
'''
#example:
try:
    lst = [10,30,56]
    index = int(input("enter the index:"))
    print(lst[index])
except ImportError:
    print("index error")
except ValueError:
    print("please entrt thr integer")
#Else: if no exception occurs
#Else: if no exception occur 
else:
    print("noexception")
'''
try:
    code
except:
    handling
else:
    succcess block 

'''
#Another example:
try:
    num = int(input("enter number:"))
    result = 100/num
except ZeroDivisionError:
    print("zero")
else:
    print(result)

'''
------------------------------------------
finally block executes always
used for:
1.closing files
2.closing database
3.cleanup code



try:
    code
except:
    handling
finally:
    cleanup code
'''
try:
    file = open("data.txt")
except FileNotFoundError:
    print("file not found")
finally:
    print("execute completed")

# example ATM Machine:
try:
    print("transaction is processing")
except:
    print("Transaction failed")
finally:
    print("thanks for using ATM")
    
try:
    a = 10/0
except ZeroDivisionError as e:
    print("error:",e)
#nested try blocks
try:
    print("outer try")
    try:
        num = int(input("Enter number"))
        print(10/num)
    except ZeroDivisionError as e:
        print("error:",e)
except:
    print("outer Exception")
#raise : used to manually 
# generate exceptions

age = int(input("Enter the age"))
if age<18:
    raise ValueError("Age should be 18 or greater")
print("Eligible")
    
#why custom exceptions:
class MyException(Exception):
    pass
# bank application:
class InsufficientBalance(Exception):
    pass
balance = 5000
Withdraw = int(input("Enter the amount"))
if Withdraw > balance:
    raise InsufficientBalance("not enough balance")
print("Withdraw successful")

#task: write a custom exception 
class Canteen(Exception):
    pass
class InsufficientBalance(Exception):
    pass
balance = 100
transaction = int(input("Enter the transaction"))
if transaction < balance:
    raise InsufficientBalance("not enough balance")
print("transaction successfull")

#student result 
class Student:
    def _init_(self,marks):
        self.marks = marks
    def calculate_result(self):
        try:
            average = sum(self.marks)/len(self.marks)
            print(average)
        except ZeroDivisionError as e:
            print("error:",e)
# t([])
# e.result()

# 
def login(self,username,password):
    try:
        if username !="admin":
            raise ValueError("Invalid username")
        if password !="admin123":
            raise ValueError("Invalid password")
        print("login successful")
    except ValueError as e:
        print("error:",e)

#Generic Exceptions:
try :
    print(10/0)
except Exception as e:
    print(e)
'''
Accept account balance and withdrawl amount 
raise Exceptions if:
1. withdrawl amount is -ve
2. withdrawl amount exceeds balance
3. withdrawl amount exceeds daily limit of 25000
4. display remaining balance if transaction successful
'''
'''
try:
    file = open("data.txt")
except FileNotFoundError:
    print("file not found")
finally:
    print("execution completed")
    









#raise: used to manually generating exception
age = int(input("enter the age:"))
if age<18:
    raise ValueError("age should be 18 or greather")
print("Eligible")


#why custom exceptions;
class MyException(Exception):
    pass


'''---------------------------------------'''
            #bank application:
class InsufficientBalance(Exception):
    pass
balance = 2345679
withdraw = int(input("enter the amount"))
if withdraw > balance:
    raise InsufficientBalance("not enough balance")
print("withdraw successful")

class SheIsNotInHome(Exception):
    pass
check = input("checking if she is inside the home")
if check.lower() == "no":
    raise SheIsNotInHome("not there")
print("she is there")'''