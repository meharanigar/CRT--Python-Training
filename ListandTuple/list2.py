#create a list with 5 frnds 
#1.add a new frnd just intaduse
#2.then remove 2 frnds
#3.then add 3 close frnds in single time
#4.sort the frnd in alpa
#5.delete the frnd index 5
#6.copy the frnd list in a new list
#7.then perform clear on pr

frnd = [10,20,30,50,60,12]
frnd.append(70)
print(frnd)
frnd.remove(10)
print(frnd)
frnd.extend([88,99,77])
print(frnd)
frnd.sort()
print(frnd)
frnd.pop(5)
print(frnd)
final = frnd.copy()
print(final)
frnd.clear()



#Nested list ?
a = [[1,2,3],[4,5,6]]# in this we have 2 index values 

#when we want to print first index first value
print(a[0][0])



#Iterating over the list

a =[10,20,30,40]
for i in a:
    print(i)

#Range()

for i in range(len(a)):
    print(a[i])


    #list comprehension:
   #[expression for variable in iterable]
   #example:
square = [x*x for x in range(1,6)]
print(square)

