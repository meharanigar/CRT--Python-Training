'''
check whether a character is alphabet or not


ch = input("enter the n:")
asci = ord(ch)
if (65 <= asci <=90) or (97 <= asci <= 122):
    print("alphabet")
else:
    print("not an alphabet")

'''

str = input("enter the char:")
count = 0
for i in str:
    count = count+1
print("lenght:",count)




