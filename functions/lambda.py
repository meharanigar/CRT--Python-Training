'''
MAP Function :
   arr = list(map(int, input().split()))

#map:
   applies the function each element of iterable
map(function,iterable)

example:
def square(x):
    return x*x
nums = [1,2,3,4]
result = list(map(square,nums))
print(result)
'''
def square(x):
    return x*x
nums = [1,2,3,4]
result = list(map(square,nums))
print(result)

#lambda
nums =[2,4,5,6]
square = list(map(lambda x:x*x,nums))
print(square)


#task: given with list of numbers 
#convert each number into cubes
#using map() and lambda
nums =[2,4,5,6]
square = list(map(lambda x:x*x*x,nums))
print(square)


