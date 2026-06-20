'''
count the frequency of the characters

explain : 
input : aaabc
output:
a:3
b:1
c:1
'''
str = input("enter the str:")
dict = {}

for ch in str:
    if ch in dict:
        dict[ch] += 1
       
    else:
        dict[ch] = 1

for ch in dict:
    print(ch," ",dict[ch])
