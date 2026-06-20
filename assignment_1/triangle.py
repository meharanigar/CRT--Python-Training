 #problem statement

# take 3 sides from user and check
# weather triangle is
#1. isosceles
#2.equilateral
#3.scalene

side = int(input("enter the  one side:"))
side2 = int(input("enter the second side:"))
side3 = int(input("enter the third side:"))

if side == side2 == side3:
    print("equilater")
elif side == side2 or side2 == side3 or side == side3:
    print("it is isoscelateral")
else:
    print("it is scalene")



'''
problem statement:

simulate the ATM system:
1.enter the pin
2. with draw only if sufficient balance is available
initial balance = 5000
             pin check
               |
               balance
               |
               withdraw the amount
'''

balance = 5000

pin = int(input("enter the pin:"))

#checking the pin
if pin == 1234:

    #withdraw amount
    amount = int(input("enter the amount:"))
    if amount <= balance:
    # deduct the amount from balancee
        balance = balance - amount

    # display the update amount 
        print("withdraw is successful")
        print("remaining balance:", balance)
    else:
        print("less amount")

else:
    print("invalid pin")


    







