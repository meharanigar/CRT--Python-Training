a =[20,60,70,10]
largest =float('-inf')
second_largest = float('-inf')
for num in a:
    if num>largest:
         second_largest = largest 
         largest = num 
    elif num>second_largest and num !=largest:
         second_largest = num
print(largest)
print(second_largest)


#TASK---> CHECK THAT THE LIST IS SORTED OR NOT
a = [5,4,9,7,54]
flag = True 
for i in range(len(a)-1):
     if a[i] > a[i+1]:
        flag = False
        break
print(flag)