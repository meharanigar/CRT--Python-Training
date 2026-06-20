n = 4
ch = 65  # A
for i in range(1, n+1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
    

# n = 4
# for i in range(1, n+1):
#     odd
#     for j in range(i):
#             print(i, end="")
#     else:
#         print(j+2, end="")
#     print()


n = 5
for i in range(1, n+1):       

    for j in range(1, i+1):     
         odd = 2*j-1     
         print(odd, end=" ")
                     
    print()

'''
n = 5
for i in range(1, n+1):

    for j in range(i):
        even += 2
        print(even, end="")
        
    print()

    n = 5
for i in range(1, n+1):
    spaces = " " * (n-i)
    stars = " ".join(["*"] * i)
    print(spaces + stars)

'''





n = int(input())
for i in range(1,n+1):
    for j in range(n-1):
          print("", end="")
    for k in range(i):
          print("*", end=" ")

    print()

        

    