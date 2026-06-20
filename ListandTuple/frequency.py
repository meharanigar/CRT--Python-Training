#find the frquency pf the element
n = int(input())
s = list(map(int, input().split()))
dict = {}

for i in s:
    if i in dict:
        dict[i] += 1
       
    else:
        dict[i] = 1

for i in dict:        # for key in dict:
    print(i," ",dict[i]) #print(dict(key))


#rotate list by k position
n = int(input())
s = list(map(int, input().split()))
k = int(input())
k = k % n
result = s[-k:] + s[:-k]
print(result)

#Alter netive method for k position
n = int(input())
s = list(map(int, input().split()))
k = k%n
for i in range(k+1):
    first = s.pop(0)
    s.append(first) 
print(s)


'''
two  pointers:
one pointer is start
one pointer is end

operations:
swapping
moves towards the center 


arr = [1,2,3,4,5.,6,12,14]
       L                R

example:
sum of any two digit should b equal to target

arr = [1, 2, 3, 4, 5, 11, 12, 18]
target = 15
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        current_sum = arr[i]+arr[j]

        if current_sum == target:
            print("pair found:",arr[i],arr[j])

'''
