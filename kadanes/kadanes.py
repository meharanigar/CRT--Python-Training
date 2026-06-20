
''' 
kadane's algorithm : max sub arrays problems
a = [2,-1,3,-2,4]
find the contigious sub array with max sum


subarrays           sum
[2]                   2
[2,-1]                1
[2,-1,3,]             4
[2,-1,3,-2]            2
[2,-1,3,-2,4]           6

kadane's algorithm main idea 
at every element we decide:
two choices:
1. continue the previous subarray
                (or)
2. start a new subarray
current_sum = -5
next_element = 10
-5+10 = 5 #discarding the previous (-ve)
next = 10

 # example 
 arr = [2,-1,3,-2,4]
 current_sum = 2
 max_sum = 2
 
 index:1
 -1 
 choice-1: extend the array 
   2+(-1) = 1
 choice-2: start a new array
 -1 
 index : 2
 
current_sum formula = max(a[i],current_sum+arr[i])
max_sum = max(max_sum,current_sum)


'''

a = [2,-1,3,-2,4]
current_sum = a[0]
max_sum = a[0]
for i in range(1,len(a)):
    current_sum  = max(a[i],current_sum+a[i])
    max_sum = max(max_sum,current_sum)
print(max_sum)



'''
problem:maximum winning streak

a cricket player gains or loses
points in each match.

positive -> won 
'''
arr=[-2,4,-1,5,-3,2]
index_start = 0
end_index = 0
tepm_start = 0
current_sum = arr[0]
max_sum = arr[0]
for i in range(1,len(arr)):
    if arr[i]>current_sum+arr[i]:
        current_sum=arr[i]
        temp_start = i
    else:
        current_sum=current_sum+arr[i]
        if current_sum > max_sum:
           max_sum = current_sum
           index_start = tepm_start
           end_index = i 
print("max_sum:",max_sum)
print(index_start)
print(end_index)
print(arr[index_start:end_index+1])


'''
problem-5
maximum product subarray

input:[2,3,-2,4]
output : 6
print(index)

'''
arr=[2,3,-2,4]
index_start = 0
end_index = 0
tepm_start = 0
current_sum = arr[0]
max_sum = arr[0]
for i in range(1,len(arr)):
    if arr[i]<current_sum+arr[i]:
        current_sum=arr[i]
        temp_start = i

        