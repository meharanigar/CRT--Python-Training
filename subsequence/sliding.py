#sliding window approch   
'''
sliding window formula:
previous_sum+(-outgoing)+incoming

'''   
arr =[2,1,5,1,3,2]
k =3
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k,len(arr)):
    #outgoing = i - k
    outgoing = arr[i-k]
    incoming = arr[i]

    window_sum = window_sum-outgoing+incoming

    max_sum =max(max_sum,window_sum)

print(max_sum)

#2.find the first continous sub array whose sum equals to the target 
arr = [1, 4, 20, 3, 10, 5]
target = 33

left = 0
window_sum = 0

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum > target:
        window_sum -= arr[left]
        left += 1

    if window_sum == target:
        print(arr[left:right+1])
        break


#find the length longest continous subarray that contains no repeating elements


arr = [1, 2, 3, 1, 2, 3, 4]

max_length = 0
unique = 0

for i in range(len(arr)):
    unique = set()

    for j in range(i, len(arr)):

        if arr[j] in unique:
            break

        unique.add(arr[j])

        length = j - i + 1
        max_length = max(max_length, length)

print(max_length)

arr = [1, 2, 3, 1, 2, 3, 4]
left = 0
right = 0
max_length = 0
unique=set()
for right in range(len(arr)):
    while right in unique:
        unique.remove(arr[left])
        left +=1
    unique.add(arr[right])
    max_length = max(max_length,right-left+1)
print(max_length)


