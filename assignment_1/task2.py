#task:2
'''
battery = int(input("enter the used hours:"))
usage  = int(input("usage battery"))
while battery > 20:
     battery = battery - usage
     hours = hours + 1
     print("hours:", hours)
     print("battery left:", battery)
     

'''





n = 5
for i in range(1,n+1):
    for j in range(n-1):
          print("", end=" ")
    for k in range(i):
          print("*", end=" ")

print()