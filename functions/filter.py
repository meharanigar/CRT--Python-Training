'''
what is filter?
selects the elements based upon the condition

syntax:
filter(function,iterable)

Example:
def is_even(x):
    return x%2==0
list = [1,2,3,4,5]
result = filter(is_even,list)
print(result)
'''
# def is_even(x):
#     return x%2==0
# list = [1,2,3,4,5]
# result = filter(is_even,list)
# print(result)
'''
#lambda
nums =[1,2,3,4,5]
square = list(map(lambda x:x==0,nums))'''

#task:given with a list frnds names
#filter the names letter starting with A
#with filter and lambda

# names = ["mehar","manasa","taslim","darshan"]
# result = list(filter(lambda x:x.startswith("m"),names))
# print(result)


'''
Reduce:
 what is reduce()?
repeatedly applies function
reduces the iterable to single value

syntax:
reduce(function,iterable)

'''
#funtools --> module
from functools import reduce
nums = [1,2,3,4,5]
result = reduce(lambda a,b:a+b,nums)
print(result)