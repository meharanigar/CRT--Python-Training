
for i in range(1,5+1):

    if i % 2 == 0:
        for j in range(i , 0 , 1):
            print(j, end=" ")
    else:
        for j in range(1, i + 2):
            print(j, end=" ")
    print()





N = int((input("enter thr input")))
for i in range(1, N + 1):
    for j in range(i):
            print(i, end ="     ")
    print()


N = int(input("enter the input"))

for i in range(N, 0, -1):
     for j in range(i, 0, -1):
          print(j, end="")
     print()

 


n = 4
ch = 65  # A
for i in range(1, n+1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
    
   