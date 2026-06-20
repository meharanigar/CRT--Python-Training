# # # #task:
# # # event = int(input("enter the number of events:"))
# # # claps  = int(input("enter thr no.of claps:"))

# # # total = sum(claps)

# # # avg = total // event
# # # print("total claps:", total)
# # # print("avg claps:", avg)



# # #task:2
# # battery = int(input("enter the used hours:"))
# # usage  = int(input("usage battery"))
# # while battery > 100:
# #     battery = battery - usage
# #     hours = hours + 1
# # print("hours:", hours)
# # print("battery left:", battery)


# #task:3

# ticket_num = int(input("enter thr ticket number:"))
# if ticket_num % 3 == 0 and ticket_num % 5 == 0:
#     print("lucky")
# else:
#     print("not lucky")


   
#task:5
#  = int(input())

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print()

# n
n = int(input())

glasses = list(map(int, input().split()))

total = 0

#count the hours
hours = 0

for glass in glasses:
    total = total + glass

    hours = hours+1

    if total > 8:
        break
print(hours)
print(total)