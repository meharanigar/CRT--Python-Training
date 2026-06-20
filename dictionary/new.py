'''
#find the frquency pf the element
n = int(input())
s = list(map(int, input().split()))
dict = {}

for i in s:
    if i in dict:
        dict[i] += 1
       
    else:
        dict[i] = 1

for i in dict:        # for key in dict:
    print(i," ",dict[i]) #print(dict(key))

'''
text = "apple banana pineapple banana apple"
words = text.split()
dict = {}
for word in words:
    dict[word] = dict.get(word, 0)+1
print(dict)


text = "apple banana pineapple banana apple"
words = text.split()
dict={}
for word in words:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
print(dict)     

'''
shallow copy:

student = {
    "name":"taslim",
    "roll.no":23
}
b = student.copy()
print(b)
'''
employee={"name":"mehar","age":24}
employee.update({"branch":"ai","phone":7095882080})
b = employee.copy()
employee.popitem()
print(employee.popitem())

employee ={
    "em1":{
        "name":"nigar",
        "age":23
    },
    "em2":{
        "name":"taslim",
        "age":34
    }
}
print(employee["em1"]["name"])

#task:
words = ["eat","tea","tan","ate","tan","nat","bat"]
groups = {}

for word in words:
    key="".join(sorted(word))

    if key in groups:
        groups[key].append(word)
    else:
        groups[key]=[word]

print(list(groups.values()))

#top k freq elements
m = [1,1,1,1,1,1,1,2,2,2,3]
k= 2
dict ={}
for i in m:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

#sort by dict descending
result = sorted(dict,key=dict.get,reverse=True)
print(result[:k])

