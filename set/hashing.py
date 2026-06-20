'''
what is hashing?
Hashing will convert data into the unique hash values


python uses:
1.hash tables
2.hash functions


unlike linear search it directle jumps to target 
with the help of hashing

search,insert,delete--->O(1)time complexity

sets operations:

1.union ---> |
2.intersection---->
3.difference
'''

#union
a = {1,2,3,4}
b = {5,6,7,8}
print(a|b)

#builting method
print(a.union(b))

#intersection
a = {1,2,3}
s = {5,2,7}
print(a&s)
#built in method
print(a.intersection(s))

#Difference 
print(a - s)
print(a.difference(s))

#symmentric difference
a = {1,2,3}
b = {2,4,3}
print(a^b)
#built in method
print(a.symmetric_difference(b))

#subset and superset
#subset:common elements in a set
a={1,2}
b={1,2,3,4}
print(a.issubset(b))
print(b.issuperset(a))

#Frozenset:immutable version of set
fs = frozenset([1,2,3,4,5])
print(fs)

'''
feature           list      tuple        dictionary    set 
ordered            yes       yes           no            no
mutability         yes        no           both         yes
allow  duplicates   yes       yes       key:no,val:all  no 
indexing           yes       yes          no            no 

'''
'''
can i store list inside the set?
1.list
2.dict
3.set
'''

# Task:
# create a list with squares of a number
# convert the list with
# squares of a number to set
# try to repeat the square two times
# add the multiple of 2 to the same  
# set at a single Time 
# --> separate the set with 2 diff sets
# multiple of 2
# squares
# now perform all the set operations on both

# Create a list with squares of numbers 1 to 5
squares_list = [x**2 for x in range(1, 6)]
print("Squares List:", squares_list)

# Convert list to set
squares_set = set(squares_list)
print("Squares Set:", squares_set)

# Try to repeat a square two times
squares_set.add(4)
squares_set.add(4)

# Create a set of multiples of 2
multiples_of_2 = {2, 4, 6, 8, 10}

# Add multiples of 2 to the same set at a single time
combined_set = squares_set.union(multiples_of_2)
print("Combined Set:", combined_set)

# Separate into two different sets
squares = squares_set
multiples = multiples_of_2

print("Squares Set:", squares)
print("Multiples of 2 Set:", multiples)

# Set Operations

# Union
print("Union:", squares | multiples)

# Intersection
print("Intersection:", squares & multiples)

# Difference
print("Squares - Multiples:", squares - multiples)
print("Multiples - Squares:", multiples - squares)

# Symmetric Difference
print("Symmetric Difference:", squares ^ multiples)

# Subset
print("Squares is subset of Multiples:", squares.issubset(multiples))

# Superset
print("Squares is superset of Multiples:", squares.issuperset(multiples))

# Disjoint
print("Are Disjoint:", squares.isdisjoint(multiples))


'''
problem:
find the lenght of longest consecutive seqence
input:[100,4,200,1,3,2]
output:[4]

'''


