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
n = int(input())
s = list(map(int, input().split()))

target = 15

left = 0
right = n - 1

while left < right:
    total = s[left] + s[right]

    if total == target:
        print("pair is found:", s[left],s[right])
        break

    elif total < target:
        left += 1

    else:
        right -= 1

#Reverse an list using two pointer approch

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = len(arr)-1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(*arr)


#check an arr is palindrome
n = int(input())
arr = list(map(int, input().split()))

left = 0
right = len(arr)-1
flag = True
while left < right:
    if arr[left] != arr[right]:
        flag = False
        break

    left += 1
    right -= 1

if flag:
    print("palindrome")
else:
    print("not palindrome")

#moves zeroes to the end of the list
n = int(input())
arr = list(map(int, input().split()))

left = 0
for right in range(len(arr)):
    if(arr[right]!=0):
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
print(arr)