# Problem Statement
# Given an array of integers, determine whether it is a sorted array rotated some
# number of times.
n=int(input())
m = list(map(int, input().split()))
count = 0
for i in range(n):
    if m[i]>m[(i+1)%n]:
        count +=1
if count <= 1:
    print("yes")
else:
    print("no")
       