#print the elements greater than previous elements
n = int(input())
w = list(map(int, input().split()))
for i in range(1,n):
    if w[i] > w[i-1]:
     print(w[i], end=" ")

#count the divisible of 3
n = int(input())
w = list(map(int, input().split()))
count = 0
for i in w:
   if i % 3 == 0:
      count += 1
print(count)

#find the absolute diff b/w the first and last
n = int(input())
s = list(map(int, input().split()))
max_diff = abs(abs(s[0]) - abs(s[-1]))
print(max_diff)

#elements which appears only once
n = int(input())
s = list(map(int, input().split()))
for i in s:
   if s.count(i) == 1:
      print(i, end="")

#move all the negative numbers to left
n = int(input())
s = list(map(int, input().split()))
positive = []
negative = []
for i in s:
   if i > 0:
      positive.append(i)
   else:
      negative.append(i)
result = negative+positive
print(result)
    
       
