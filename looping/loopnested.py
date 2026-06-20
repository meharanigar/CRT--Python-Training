# '''
# nested loop: loop inside the loop
# first loop: outer loop---> row
# second loop: inner loop---> column

# example program :
# '''
# i= 1 
# while i<=3:
#    j = 3
#    while j<=2:
#       print(i,j)
#       j = j + 1
#    i = i + 1

# """
# how nested loop works using for:
# for i in range(1,4): i = 4

# for j in range(1,3): j=3 

#  print(i,j) print(1,1)(1,2)
#             print(2,3)(2,2)
#             print(3,1)(3,2)

# """


# '''
# note: outer loop runs once 
#       inner loop runs completely
#    outer loop runs twice
#      inner loop runs completely

#      why nested loops are used :
#      1. pattern problems  ---> for pattern problems for loop is best
#      2. matrix operations
#      3. tables
#      4. grid systems
#      5.games
#      6. comparing the elements

# '''
# '''
# *****
# *****
# *****
# *****
# '''
for i in range(5):
    for j in range(8):
        print("*", end = "")
    print()







for i in range(1,6):
    for j in range(i):
        print("*", end = "")
    print()





for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


for i in range(5, 0, -1):
     for j in range(i):
         print("*", end = " ")
     print()



