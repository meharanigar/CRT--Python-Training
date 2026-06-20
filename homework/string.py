#find the longest substring without repeating any character
ch = "abcabcbb"
left = 0
right = 0
max_length = 0
unique=set()
for right in range(len(ch)):
    while ch[right] in unique:
        unique.remove(ch[left])
        left +=1
    unique.add(ch[right])
    max_length = max(max_length,right-left+1)
print(max_length)
