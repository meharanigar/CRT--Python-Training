'''#1. find the max in tuple
s = [1,23,4]
max =0
for i in s:
    if(i>max):
        max = i
print(max)


#2.convert the tuple in list
t = (1,2,3)
a = list(t)
print(a)

#3. find the avg of the number in a list
#note: take the input from the user
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    count +=i
avg = count / n
print(avg)

#4.find the all odd num in list
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if i % 2 != 0:
        print(i, end="")

#find the sum of the each element in list
n = int(input())
a = list(map(int, input().split()))
for i in a:
    temp = i
    total = 0
    while temp > 0:
        total = total+temp % 10
        temp = temp // 10
    print(total)

    #find the smallest even num in a list
n = int(input())
a = list(map(int, input().split()))
small = a[0]
for i in a:
    if i % 2 == 0 and i <= small:
     print(i)
        

#sum of elements
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    count += i
print(count)'''

#8.find the num of elements greather than avg
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    count += i
avg = count/n
print(avg)
for i in a:
    if i > avg:
        print(i)
'''
this is the built function  for sum

n = int(input())
a = list(map(int, input().split()))
avg  = sum(a) / n
print(avg)'''
'''
#find the largest and smallest number in a list
n = int(input())
a = list(map(int, input().split()))
max_num = a[0]
min_num = a[0]
for i in a:
    if max_num >= i:
        max_num = i
    if min_num <= i:
        min_num = i
print(max_num)
print(min_num)
result = max_num - min_num
print(result)

#count the number ending with 5

n = int(input())
t = list(map(int, input().split()))
count = 0
for i in t:
    temp = i
    if(temp%10==5):
        count = count+1
    print(count)
'''

#replace the negative numbers with zeros
n = int(input())
t = list(map(int, input().split()))
for i in a:
    if(i<0):
        a.replace(0)
print(a)