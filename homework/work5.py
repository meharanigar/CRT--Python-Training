
#You are given two sorted arrays. Merge them into a single sorted
#array using the Two Pointers technique.
n = int(input())
s1 = list(map(int, input().split()))

m = int(input())
s2 = list(map(int, input().split()))

i = 0
j = 0
merged = []

while i < n and j < m:
    if s1[i] <= s2[j]:
        merged.append(s1[i])
        i += 1
    else:
        merged.append(s2[j])
        j += 1

while i < n:
    merged.append(s1[i])
    i += 1

while j < m:
    merged.append(s2[j])
    j += 1

print(*merged)