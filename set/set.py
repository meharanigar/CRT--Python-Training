'''
SET:collection of unordered unique elements
-- unordered
-- unique(never allows duplicates)
-->fast searching O(1)
-->no fixed indexing

why we use:
1.O(1)
2.duplicates removel

how to create a set?
set = {1,2,3,4,5}
'''
set = {1,2,3,4,5}
print(set)

#check duplicates
s = {1,1,2,2,3,3,4,5,6}
print(s)

s = {1,1,2,2,3,3,4,5,6}
unique =set(s)
print(unique)


#1st method--->create
num ={1,2,3,4}

#2nd way-->create
s = set([1,2,3,4,5])

# creating empty set
s =set()
s.add(1)
print(s)

#adding multiple elements 
s.update([2,3,4,5])
print(s)

#to remove the elements
s.remove(3)

#discard:
print(s.discard(10))

#pop():delete random element
s.pop()
print(s)

#clear the all elements--->s.clear()


