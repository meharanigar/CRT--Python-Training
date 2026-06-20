t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    for k in range(1, n + 1):

        match = True

        for i in range(n):
            j = (i + k) % n

            if s[i] != s[j]:
                match = False
                break

        if match:
            print(k)
            break