'''
prefix sum: one of the most importent techniqye used
to solve sub array problems
1.fast range sum queries
2.Optimization
3.sliding window ulternative
4.sub array problems
5.competitive programming

-->reduces the repeated 
and improves the time complexity

what is prefix sum?
stores the cumulative sum of the elements
from the beginning of the array to every index

arr = [a0,a1,a2,a3....]

then:
the prefix of i will become
prefix[i] = arr[0]+arr[1]+arr[2]+.....arr[i]
'''

#problem:

# find the sum from index 1 to 3  general  code
arr = [10, 20, 30, 40, 50]
# index: 0 1 2 3 4

sum = 0
for i in range(1, 4): 
    sum += arr[i]

print(sum)

# prefix sum --->
arr = [2,4,1,7,3]
#      0 1 2 3 4
#calculate the prefix:
#index   arr[i]  prefix[i]
# 0       2        2
# 1       4       2+4
# 2       1       6+1
# 3       7       14
# 4       3       17

#prefix[1] = [2,6,7,14,17]

'''
prefix[0] = 2 sum from 0 to 0
prefix[1] = 6 sun orom 0 to 1
prefix[2] = 7 sum from 0 to 2
prefix[3] = 14 sum from 0 to 3
prefix[4] = 17 sum from 0 to 4
'''

'''
prefix sum formula:
sum = prefix [R] - prefix[L-1]

find sum from 1 to 3
R = 3
L = 1
sum = prefix[3] - prefix[0]
sum =
'''
arr = [2,4,1,7,3]
n = len(arr)
#create prefix array 
prefix =[0]*n
prefix[0] = arr[0]
#[2,0,0,0,0]
#build the prefix
for i in range(1,n):
    prefix[i] = prefix[i-1]+arr[i]
print(prefix)
L = 1
R = 3
#range sum
if L == 0:
    ans = prefix[R]
else:
    ans = prefix[R] - prefix[L-1]
print(ans)
    
#find the multiple range queries
#1-4
#2-5
#0-3


arr = [2,4,1,7,3]
n = len(arr)
#create prefix array 
prefix =[0]*n
prefix[0] = arr[0]
#[2,0,0,0,0]
#build the prefix
for i in range(1,n):
    prefix[i] = prefix[i-1]+arr[i]
print(prefix)
s = [[1, 4], [2, 4], [0, 3]] 

for L, R in s:
    if L == 0:
        ans = prefix[R]
    else:
        ans = prefix[R] - prefix[L-1]  
    print(f"Sum from {L} to {R} = {ans}")

'''
problem.3:
find the equilibrium index using prefix sum

arr = [1,3,5,2,2]

left sum = 1+3=4
rightsum = 2+2=4

left sun == right sum
 
 '''
arr = [1,3,5,2,2]
n = len(arr)
prefix =[0]*n
prefix[0] = arr[0]
for i in range(1,n):
    prefix[i]= prefix[i-1]+arr[i]
total = prefix[n-1]

for i in range(n):
    if i==0:
        left=0
    else:
        left=prefix[i-1]

    right=total-prefix[i]

    if left==right:
        print("Equilibrium Index =",i)
        break




