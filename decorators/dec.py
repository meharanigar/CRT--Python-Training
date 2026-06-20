'''
Decorators:
adds the extra functionality
without changing the original function

Gift Wrapper:
extra layer, beauty

decorator = wrapper around the function

-----------------------------
#why decorators are needed?
logging:
authentication,
timing
validation

---------------------------

if no decorators
1.repeated code
2.messy prigrams
--------------------------
'''
#in python ---> functions are treated like variables

def greet():
    print("hello mehar")
x = greet
x()

#nested functions
def outer():
    def inner():
        print("inner side")
    inner()
outer()

#returing the function
def outer():
    def inner():
        print("inner side")
    return inner
x = outer
'''
outer
|
returns the inner
|
stored in x
|
x()
'''
#simple decorators
def decorators_function(original_function):
    def wrapper():
        print("------------")
        original_function()
        print("************")
    return wrapper

#original function
def greet():
    print("hello nigar")

#apply manually
decorated = decorators_function(greet)
decorated()

#EXAMPLE2:
def smart_divide(func):
    def wrapper():
        print("before checking the division ")
        func()
        print("Division is completed ")
    return wrapper 
@smart_divide
def divide():
     print(10/2)
divide()
'''

'''

#example:3
@decorators_function
def greet(name):
    print("hello",name)


#Example:login checking 
def login_required(func):
    def wrapper():
        print("checking the user login")
        func()
    return wrapper
@login_required
def dashboard():
    print("Welcome to dashboard")
    
dashboard()