'''
proble
'''

m = [1,2,3,4]
total = 0
for i in m:
    total = total+i
print(total)
#time complexity: O(n)
'''
2.find max element in a list
'''
n = [10,20,30,5,60]
max = n[0]
for i in n:
   if (i>max):
       max = i
       
print(i)
'''
3.count the even numbers in list
'''
n = [1,2,3,5]
count = 0
for i in n:
    if i % 2 == 0:
        count += 1
print(count)

'''
4.reverse the list
'''
v = [1,2,3,4,5]
v.sort()
print(v)
v.reverse()
print(v)

'''
5.remove the duplicates
'''
v = [1,2,2,3,4,5,5]
result = []
for i in v:
    if i not in result:
        result.append(i)
print(result)

'''
6.find second largest num
'''
# num = [12,45,78,34]
# max = [0]
# for i in num:
#     if i > max:
#         max += i



'''
7.check if list is sort with out using inbuilt methods
'''
n = [1,3,2,6,5]
result = 0
for i in n:
    if(n>i):
        result += i
print(result)
    
#8.find the largest odd number:
list = [1,2,3,4,5,6,7,8,9]
large = 0
for i in list:
    if i % 2 != 0 and i > large:
        large = i
print(large)


#9.create a list of 
list = [1,2,3,4]
m = 0
for i in list:
    m.append(list*list)
print(m)

    