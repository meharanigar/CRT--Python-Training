


# s = input("enter the s:")
# result = ""

# for i in s[::-1]:
#     if i.islower():
#         result += i.upper()
#     else:
#         result += i.lower()

# print(result)


'''

str = input("enter the str:")
result =" "
for ch in str:
    if ch.isalpha():
     result = result+ch
print(result)
'''

  #with build functions
# n = input("enter the n:")
# result = ""
# for ch in n:
#    if n.replace(""," "):
#       result = result+ch
# print(result)
      

#with out using build functions
'''
text = input("Enter string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print(result)'''

'''
p = input("eneter the p:")
result = " "
for ch in p:
   if ch not in "{}[]()":
      result = result+ch
print(result)
  


s = input("enter the s:")

result= 0
for ch in s:
   if ch.isdigit():
      result +=int(ch)
print(result)'''

#task:capital the first and last letter of the string
m = input("enter the m:")
result = []
words = m.split()
for word in words:
   if len(word) == 1:
      result.append(word.upper())
   else:
      new_word = ( word[0].upper()+word[1:-1]+word[-1].upper())
      result.append(new_word)

print("".join(result))








