# salary = int(input("enter the the amount"))
# ex = int(input("enter the experience"))

# bonus = 675.0

# print(bonus)

# final = salary + bonus

# print(final)




value = int(input("enter thr value:"))

if value % 5 == 0:
    print("divicion")
else:
    print("no")



#leap year print 

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


#problem statement:

#calculate the electricity bill using the conditions:
#1,first 100 units --> 5/unit
#2.next 100 units --> 7/unit
#3.above 200 units---->10/unit


unit = int(input("enter the used units:"))

if unit <= 100:
    bill = unit * 5
elif unit <=200:
    bill = (100 * 5) + ((unit - 100) * 7)

else:
    #first 100 unit---5
    #next 100 un it --7
    #above 200 unit---10
    bill = (100 * 5) + (100 * 7) + ((unit - 200) * 10)

#display thr whole bill
print("final bill:" , bill)


