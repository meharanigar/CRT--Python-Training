num = input("enter the num:")
freq = {}

for ch in num:
    if ch in freq:
        freq =+ 1
    else:
        freq = 1

max_char=" "
max_count=0
for key in freq:
    if freq[key]>max_count:
        max_count = freq[key]
        max_char = key
    
    print(max_count)
    
