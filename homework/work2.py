#Tuple Boundary Product
n = int(input())
t = tuple(map(int, input().split()))
product = t[0]*t[-1]
print(product)


# replace the negative numbers with zeros
n = int(input())
t = list(map(int, input().split()))
for i in range(n):
    if t[i] < 0:
        t[i] = 0

print(*t)

#product of all elements
n = int(input())
s = list(map(int, input().split()))
product = s[1]*s[1]
print(product)

