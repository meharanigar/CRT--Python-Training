
'''
1
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print((i + j + 1) % 2, end="")
    print()
'''

'''
2.
n = int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j == n-1:
            print("*", end=" ")
        else:
            print("_", end=" ")
print()
'''

'''
3.
n = int(input())
for i in range(1,n+1):

    if i % 2!= 0:
        for j in range(1, i+1):
            print(j, end="")
    else:
        for j in range(1,0,-1):
            print(i, end="")
    print()

'''

'''
4.
n = int(input())
for i in range(1,n+1):
    for j in range(i, n-1):
        print(j, end="")
    print()

'''

'''
5.
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end="")
    print()
'''

#8.find the largest odd number:
list = [1,2,3,4,5,6,7,8,9]
large = 0
for i in list:
    if i % 2 != 0 and i > large:
        large = i
print(large)

#9.create a list of 
i = [1,2,3,4]
m = []
for i in i:
    m.append(i*i)
print(m)

#10.check whether the  given number is exist in the  list
i = [1,2,3,4,5]
target = 3
found = False
for i in i:
    if i == target:
        found = True
        break
if found:

    print("element found")
else:
    print("not found")

#11.find the common elements in both the list
a = [1,2,3,4,5]
b = [6,7,1,8,9]
for i in a:
    if i in b:
        print(i)

#12.swap the first and last elements in list
s = [1,2,3,4,5]
s[0], s[-1] =a[-1],a[0]
print(s)



