#2.find the first continous sub array whose sum equals to the target
arr =[1,4,20,3,10,5]
target = [33]
for i in range(len(arr)):
    sum=0
    for j in range(i, len(arr)):
        sum = sum+arr[j]

    if sum == target:
        print(arr[i:j+1])



#using sliding window
arr = [1,4,20,3,10,5]
target = 33
sum = 0 


#count t
#using two pointers
n = int(input())
s = list(map(int, input().split()))
k = int(input())
s.sotr()
pair = set()
left = 0
right = n-1
current_sum = 0
while left<right:
    current_sum == s[left]+s[right]
    if current_sum == k:
        pair.add((s[left],s[right]))
        left +=1
        right -=1
    elif current_sum < k:
        left +=1
    else:
        right -=1
print(len(pair))
