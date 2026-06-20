n=int(input())

words=[]
for i in range(n):
    words.append(input())

if len(set(words))!=n:
    print("INVALID")
else:
    valid=True

    for i in range(n-1):
        if words[i][-1]!=words[i+1][0]:
            valid=False
            break

    if valid:
        print("VALID")
    else:
        print("INVALID")