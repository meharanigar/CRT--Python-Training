'''
list = list is the collection of ordered elements

list = is mutable

Allow's duplicate---> yes list allows duplicate
#dynamic in size
#syntsx: list_name = []

#stores hetrogenous elements

we can store multiple data types in list
'''

m = [12,12,13,14]
print(type(m))

#accessing the elements

a = [10,20,30,40]

print(a[0])


#check the mutability

a[0] = 60

#negative indexing
a = [10,20,30,40]
#    -4 -3 -2 -1
print(a[-1])
print(a[-2])

#Slicing:
#list[star:end:step]
print(a[0:3])
print(a[::2])

#List method

#append:
a = [10,20,30,40]
a.append(30)
print(a)

#adding multiple elements using (extend)
a.extend[50,60,70]
print(a)

#insert---> this method is add in the specific index
a.insert(2,89)
print(a)
#remove --->removes the elements
a.remove(20)
print(a)

#pop -->removes the elements with index 

a.pop(0)

#clear--> deletes all elements
a.clear()

#index() : returns the position
print(a.index(20))

#count() : count the occurances of the element

print(a.count(20))

#reverse():
a.reverse()

#copy(): it copy the one list and print the another list
b = a.copy()
print(b)

#Sorting in list:
a = [5,0,7,4,6]
#sot()-->sorts in ascending order
a.sort()
print(a)

#Descending order : first sort the list and then reverse the list
a.sort(reverse=True)
print(a)

#sorted: creates a new list
a = sorted(b)
print(a)

'''
Tuple:collection of  ordered elements
#immutable
#Tuple: more faster than list
allow's duplicates

feature    list   tuple
mutable     yes    no
duplicate   yes    yes
ordered     yes    yes
performance  slow  fast
syntax       []     ()
'''
t = (1,2,3,3.2)
print(t)
print(t[0])


#Tuple pack and unpack

 #packing
t = (10,20,30)
#unpacking
a,b,c = t
print(a)
print(b)
print(c)

#tuple methods: 1. count()
 #                2.index()

t.count(10)
t.index(20)

'''
we use tuple when we have fixed data
list : we have dynamic data

1.can tuple consist of a list?
yes

2.what is the diff between append and extend?
append: indivodual element
extend: multiple elements
'''

t = ([1,2,3],10,2.9)
t[0].append(20)
print(t)

a =[1,2,4]

a.append([5,6,7])
print(a)