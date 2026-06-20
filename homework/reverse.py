#reverse the k position in a list using//pointers 
n = int(input())
s = list(map(int, input().split()))
k = int(input())
k = k%n
def reverse(s,left,right):
    while left<right:
        s[left],s[right]=s[right],s[left]
        left +=1
        right -=1
reverse(s,0,n-1)
reverse(s, 0, k-1)
reverse(s, k, n-1)
print(*s)
    



    