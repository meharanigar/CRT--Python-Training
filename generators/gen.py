'''
youtube: doesn't loads the whole video
loads by:
small chunks
when needed

simply grnrrators works in the same for

problem with list:
list =[1,2,3,4,5]

entire list is stored in memory

nums = [i for i in range(100000)]
python consumes :
high memory
slower

Generators:
produces values one at a time
only when it is needed
saves memory

in generator we use yield 
yiled keyword:
yield paused the function
and remembers the state
'''
#yield: paused the memory

#example:
def num():
    yield 1
    yield 2
    yield 3
x = num()
print(x)

#access the numbers
print(next(x))
'''

'''

#Generators:
'''remember the variables
    remember line position 
    continue from the same place
'''

#Difference btw the return and yield
'''
Return                                yield
ends the function                    pauses the function
returns the single val               pauses the multiple values
by one                                
no state memory                      remembers the memory
'''
def test():
    return 1
    return 2
    return 3
print(test())

def num():
    yield 1
    yield 2
    yield 3
x = num()
print(x)

#using for loop
#for loop uses iter() and next() internally
def numbers():
    yield 1
    yield 2
for i in numbers():
    print(i)


#create a generator for the even numbers
def num(limit):
    num =2
    while num <= limit:
        yield num
        num+=2
x = num(10)
for i in x:
    print(i)

#memory efficiency
'''
Generator
nums = (i for i in range(1000000))
only the current value
'''
#Lazy evaluation
'''
values are generated when neede
generators are lazy
'''

#write program for fibonacii using generators
def fibo(limit):
    #first two numbers 
    a = 0
    b = 1
    #loop untill the limit 
    while a<= limit:
        #generate the current value
        yield a
        #update the values
        a, b = a+b
x = fibo(20)
for i in x:
    print(i)