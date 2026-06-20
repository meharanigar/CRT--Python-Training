n = int(input())
s = list(map(int, input().split()))
k = int(input())
k = k % n
result = s[-k:] + s[:-k]
print(result)

#Problem 2: Find Missing Number
n = int(input())
s = list(map(int, input().split()))
count = n*(n-1)//2
given = sum(s)
print(count-given)

#Problem 3: Maximum Difference Between Two Elements
n = int(input())
s = list(map(int, input().split()))

min_val = s[0]
max_diff = s[1] - s[0]

for i in range(1, n):
    max_diff = max(max_diff, s[i] - min_val)
    min_val = min(min_val, s[i])

print(max_diff)

#problem 4:
n = int(input())
arr = list(map(int, input().split()))

sorted_flag = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        sorted_flag = False
        break

if sorted_flag:
    print("Sorted")
else:
    print("Not Sorted") 