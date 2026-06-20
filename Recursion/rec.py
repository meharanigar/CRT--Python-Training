'''
Recursion is a programming technique where
a function calls itself to solve smaller version of the problems

function--> calls itself-->again-->again


1.Base case
condition where the recursion

2.Recursive case:
function calls it self with a smaller input
'''
def hello(n):
    if n==0:  #base condition
        return
    print("sorry")
    #recursive case
    hello(n-1)
hello(10)

#fibonacci:
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(10))

#problem:3
#reverse a string
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("nigar"))

#unwinding ---> retutning face

#task:4
#given with n = 1234
#perform the sum of all the digit
def digit(n):
    if n==0:
        return n
    return n % 10 + digit(n // 10)

print(digit(1234))

#problem:5
#check palindrome string using recursion
#input:madam
#output:true
def pal(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return pal(s[1:-1])

print(pal("madam"))


#problem:5
#find the largest element in an array  using recursion
def find_max(arr,n):
    if n == 1:
        return arr[0]
    return max(arr[n-1],find_max(arr,n-1))
print(find_max)


'''
check array is sorted or not using recursion
input:[1,2,3,4,5]
output: true
'''
