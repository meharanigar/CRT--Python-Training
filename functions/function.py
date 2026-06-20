'''
what is function?
ans: function is a block of reusable code.performs
specific task

why functions?
1.Avoid repetition
2.Improves readabilty
3.Easy Debug
4.Modular programming


#funtion definition

def function_name(parameters):
    """DOC STRINGS"""
    statements
    return value

'''

#def ---> keyword
'''
function_name--->identifiers
'''
#parameters--->input to the function

#Return ---> output
'''
#function calling: executing the code

function_name()
'''
#create a function
def hello():
    print("Hello World")
#call the function 
hello()

# functions are two types :
# 1. Built in functions         2. User defined functions

'''
1. Built in functions:                2.user defined function:
which are already defined              in this we will create our logic
ex: print()                              as per our requirements
input(),max(),min()

'''
#parameters:variable passed during the function definition

def add(a,b):#a,b are parameters
    return a+b

#arguments = values passed during the function call
#calling the function
add(2,3) # 2,3 --- arguments

'''
Types of arguments:
1.Positional arguments

'''






#create a functin to calculate the simple interest using positional arguments
'''def intrest(p,r,t):
    print(p*r*t)/100
intrest(p=100,r=20,t=2)
print(intrest)
'''

#3.Default arguments:
def square(a,power=2):
     print(a**power)
square(4)

'''
#variable lenght arguments
def total(*args):
    print(args)
#call function
total(10,20,30)
'''
def total(*args):
    print(args)
    print(sum(args))
#call function
total(10,20,30)


#create a function to fined sum of any number of values
def total(*a):
    print(sum(a))
total(10,20,40)

'''
kwargs -->keyword arguments
'''
def student(**kwargs):
    print(kwargs)
student(name="mehar",branch="ai",roll="8")

#create a function to print employee details 
def employee(**kwargs):
    print(kwargs)
employee(name="mehar",roll="12",phone="7095882080")

#write args and kwargs together
def student(*a,**kwargs):
    print(sum(a),kwargs)
student(10,20,name="mehar")

'''
Return statement:send the values back to the caller

def add(a,b)
    return a+b
result = add(10,20)
print(result)

print                      |                 return
display the output         |               send the value
cannot reuse               |              can reuse
                           |                     
'''
#multiple return values:
def cal(a,b):
    return(a+b,a-b,a/b)

#formet:tuple
s,sub,div = cal(20,30)
print(s,sub,div)

#task: create a function that return multiple values
def numbers(a=10,b=20,c=30,d=40):
    n = 4
    minimum = min(a,b,c,d)
    print("mini",minimum)
    maximum = max(a,b,c,d)
    print(maximum)
    total = a+b+c+d
    avg = total/n
    print("average",avg)
numbers()

'''
def add(a,b)
""" this function adds two numbers"""
return a+b
'''
def add(a,b):
    """ this function adds two numbers"""
    return a+b
print(add.__doc__)
print(help(add))


#task: create a docstring for the simple intrest program
def simple_interest(p, r, t):
    """Returns the simple interest for given principal, rate, and time."""
    return (p * r * t) / 100

#Gloabal scope:outside the function
x = 100
def show():
    c = 20
print(x)
show()

#accessing the local variable outside the function
x =0
def update():
    global x
    x = x+5
update()
print(x) # 5

#without using global
x = 0
def update():
    x =x+5
update()
print(x)

'''
task:
create a function bank_transaction
which accepts:
1.account holder
2.balance
3.transaction type(deposit/withdraw)
4.amount

use:
default arguments
return statement
'''
def bank_transaction(name="kavya"):
    balance = int(input("Enter the balance: "))
    transaction_type = input("Enter the type (deposit/withdrawal): ")

    if transaction_type == "deposit":
        deposit = int(input("Enter the amount: "))
        balance = balance + deposit
        print("Updated balance =", balance)

    elif transaction_type == "withdrawal":
        withdrawal = int(input("Enter the amount: "))

        if withdrawal > balance:
            print("Insufficient balance")
        else:
            balance = balance - withdrawal
            print("Updated balance =", balance)

    else:
        print("Invalid transaction type")

bank_transaction()