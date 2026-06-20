#Missing Badge Detection
n = int(input())
s = list(map(int, input().split()))
dict = {}
unique_id = set()
for i in s:
    dict[i]=dict.get(i,0)+1
   
for i, count in dict.items():
    if count == 1:
        unique_id.add(i)
print(*sorted(unique_id))


n = int(input())
s = list(map(int, input().split()))
dict = {}
count = ()
for i in s:
    dict[i]= dict.get(i,0)+1
for mark, count in dict.items():
    print(mark, count)


#unique fruit
n = int(input())
fruits = input().split()

unique_fruits = sorted(set(fruits))

print(*unique_fruits)



#intersection
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(a & b)