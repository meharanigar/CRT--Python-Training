'''
what is a loop ?
a loop is used to repeat the block of code
instead of 


print("Hello)
print("Hello)
print("Hello)
print("Hello)

'''
#looping --- > 2 type
 #   /             \
    #for           while

'''
for ---> used when the num of iterations is known
while ---> num of iteration are unknown


benifits:
1. reduce the code duplications & complexities
2.save time
3.make our program very efficient
4.


execution flow of loop:
    start 
      |
    condition check
   
           |
    True  -->execute the block  
           |
           repeat
           |
           false----> stop

           
           python:
    list is a collection of ordered elements
    list ---> [,,,,,,]
   list is mutable

'''

frnds = ["mehar","vijaya","nigar"]


# #syntsx:

# for var in sequence:
#     statement

for frnd in frnds:
    print(frnd)
#2nd way ? 
#range (start,end-1,step)
#range(1,11)

for i in range(5):
    print(i)

for i in range(1,16):
    print(i)



#task: mutiplication table using for loop
for i in range(1,11):
    print("5 x", i, "=", 5 * i)



sum = 0
for i in range(1,6):
    sum +=i
    print(sum)


#task: "mehar nigar" now count char in your name

m = "mehar nigar"

for i in m:
    print(i)

#task:
for i in range(2,21,2):
    print(i)
   
#task : reverse of the sequence

for i in range(11,1,-1):
    print(i)


#while condition:
# statement

#example:
# i = 5
# while i <=5:
#     print(i)

# looping   


# while True:
#     print("run forever")

#sum of numbers ---> using while

num = int(input())
total = 0
while num != 0:
    total = total + num 
    num = int(input())
print(total)

for i in range(2, 21):
    print(i)




