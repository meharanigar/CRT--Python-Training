'''
loop control: 

Break: it stops the execution of the loop immediatly
(Terminates the loop immediatly)

continue : skips the current iteration

pass: it do's nothing

'''

'''
Q2: what makes the loop infinite ?
when condition never mets false becomes an infinite

Q3: can we use else with while ?
i = 1
while i <= 3:
     print(i)
     i += 1
else: 
    print("loop is finished")


NOTE: else wont work if there is a break statement

'''


# example: break 

i = 1

while i<=10:
    if i == 5:
        break # terminates at 5 
    print(i)
    i += 1
#continue:skips the current iteration and moves forwords

for i in range(1,11):
    if i == 5:
        continue
    print(i)


#pass: do's nothing (provides a place holder for the code) 
for i in range(1,11):
    pass



num = 10
while num >= 10:
    if num == 5:
        break
    print(num)
    num -= 1
for num in range(1,10):
    if num == 6:
        continue
        pass




