for i in range(1, 6 + 1):
    for j in range(1,i-1):
        if j % 2 == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()



N = (input())
for i in range(1,N+1):
    for j in range(1,i+N):
        
        if j % 3 == 1:
            print(1, end="")
        else:
            print(2, end="")
    print()