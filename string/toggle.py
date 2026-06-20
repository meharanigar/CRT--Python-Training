'''
Toggle each charecter:
Python ---> 
'''

text = input("enter the str:")
result = " "
for ch in text:
    if ch.isupper():
        result = result+ch.lower()
    
    else:
        result = result+ch.upper()
        print(result)



'''
Remove the vowels from the str
vowels" a e i o u

'''
# text = input("enter the str: ")
# result = ""
# vowels = "aeiouAEIOU"   # include uppercase too

# for ch in text:
#     if ch not in vowels:
#         result = result+ch

# print(result)


str = input("enter the str:")
result = " "
for ch in str:
    if ch.lower() not in ['a','e','i','o','u']:
        result = result+ch
print(result)


'''
check anagram

input: SILENT---->LISTEN

'''

