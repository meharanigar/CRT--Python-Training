'''n = int(input("Enter the number"))
freq = {}
count = 0
for i in range(n):
     if i in freq:
           count = count+1
           freq.append(i)
     else:
           count = 1
print(count)
print(freq)
print(freq.lower())
'''
num = int(input("Enter the number : "))
count = 0
for i in range(1,num):
     if( i % 3 == 0 and i % 5 == 0):
           count = count +1
print(count)


