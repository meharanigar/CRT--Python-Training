#task:1

n = int(input())
arr = list(map(int, input().split()))
def product(arr, n):
    if n == 1:
        return arr[0]
    return arr[n - 1] * product(arr, n - 1)


print(product(arr, n))


#task:2
n = int(input())
def binary(n):
    if n == 0:
        return

    binary(n // 2)
    print(n % 2, end="")
if n == 0:
    print(0)
else:
    binary(n)