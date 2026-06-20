'''
Analogy:
You are given with 2 programs where it is generating the same output

how will you decide which one to use?
1.faster program
2.less memory
3.efficient

alorithmic complexity == efficient

two types:
1.Time complexity:faster results in google
2.Space complexity:

 mark-zukerberg

 TIME COMPLEXITY: measures how the runing time grows as the size of input

 3 -- to measure this  time complexity
 1.
 
'''

import time

start = time.time()
#stop watch method:

for i in range(1,101):
    print(i)

print(time.time()-start)

'''
problems in above technique


1. different system diff time
2. different compilers/diff interpreters
3. background apps effects time
4. internet/cpu/gpu affect the performance
'''

#technique- 2 counting the num of operations

#not measure the time in seconds but counts the num of operations in 

def  c_to_f(c):
    return c*9/5+32

#example-2:
def mysum(x):
    total = 0
    for i in range(x+1):
        total = total+i
    return


#Technique--3 order of growth

'''
Notations:
Asymptotic notations


1. Big oh O():calc the upper bound(worst time complexity)
2. Omega notation : best case complexity
3. Thete : avg case complexity

#example : linear search
arr = [1,2,3,4,5,6,7]

arr[0] == target #best case
arr[4] == target #avg case
arr[last] == worst case



Big O notation :worst time growth
focus:
1.measuring the scalability
2.machine independent
3.focuses on growth
4.ignores the hardware




#example-2:
def mysum(x):
    total = 0
    for i in range(x+1):
        total = total+i
    3 1+2n x=10--->21 operations



Big oh (rules)
1.additive constant(remove)
#1+2n ---> 2n

2.multiplicative constant(remove)
#2n ---> n 
   
time complexity --->O(n)


time complexity ---> O(n)

a = 10
b = 20
c = a+b

for i in range(1,101):

o(n)

    for i in range(n,n+1):
        for j in range(i):
           print(i)

eduaction : n^2+n=10 --> n^2+n ---> o(n^2)-----> for nested loops

for i in range(n,100)
    print(i)

fot j in range(1,50):
print(j)

n+n ---> 2n ---> 0(n)

1.n^2+10000n+3^1000

'''
#complexity classes
'''
1.constant time -->O(1)
 _>same time always 

 arr=[10,20,30]

 
 
 '''

'''
 Space complexity : measures the memoty uswed by the alorithim

 1.input space
 2.Auxiliary space

 example:
 a = 10
 b = 20

 constant space--->O(1)

 example-2:

 arr = [0]*n

 linear space --->O(n)
 '''