'''
sub arrray : it should have a continuity
derived from continuous part 
[1]
[1,4] wrong
[4,5,6]----> yes 
# sub sequence : where the elements are skipped and doesnt have a continuity
select any elements 

concept            subarray           subsequence

continuity           yes                   no
skipping allowed      no                    yes
derived order        continuous              sel

ex : [1,2,4,5,6,7,9,11]
subarray: [1,2,4]
subarray: [4,5,6,7]

subsequence:[1,2,4,5]
'''
#1.arr = [2,1,5,1,3,2]
n = int(input())
s = list(map(int, input().split()))
k = 3
max_sum = 0
for i in range(n-k+1):
    current_sum = 0
    
    for j in range(i,i+k):
        current_sum = current_sum+s[j]
print(max_sum)


