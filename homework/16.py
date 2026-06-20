#task:1--> robot problem
t = int(input())
n = int(input())
s = list(map(int, input().split()))
prefix = 0
min_sum = 0
ans = float('-inf')
for i in range(n):
    if i%2==0:
        val = s[i]
    else:
        val = -s[i]
        prefix+=val
        ans = max(ans, prefix-min_sum)
        min_sum=min(min_sum,prefix)
print(ans)
