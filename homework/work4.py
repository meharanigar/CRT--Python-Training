# problem 8
# Given a sorted array and a target value K, find the pair whose sum is
#closest to K. Use the Two Pointers approach.
# solution:
n = int(input())

arr = list(map(int, input().split()))

k = int(input())

left = 0
right = n - 1

min_diff = float('inf')
best_pair = ()

while left < right:

    current_sum = arr[left] + arr[right]

    diff = abs(k - current_sum)

    if diff < min_diff:
        min_diff = diff
        best_pair = (arr[left], arr[right])

    if current_sum < k:
        left += 1
    else:
        right -= 1

print(best_pair[0], best_pair[1])