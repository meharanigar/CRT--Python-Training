'''
Iterators:
gives one element at a time based upon demand

python referes this iterators:
memory efficiency
controlled access

Iterable: is an object can be looped
1.list
2.tuple
3.set
4.dict
5.string

Examples:
nums = [10,20,30,40]
for x in nums:
    print(x)

syntax:
iterable_object = [1,2,3,4]
it = iter(iterable_object)
print(it)
print(next(it))

iterable--->iterator                    


How loop in python works internally
iterators-->will be used internally
iter(),next()


   List
    |
    iter()
    |
    iterator
    |
   [1,2,3,4]

nted then pause
print(next(it))#resume

nums = [1,2,3,4]
it = iter(nums)nums = [1,2,3,4]
   it = iter(true)
   while true:
       try:
          x = next(it)
          print(x)
        except stop iteration:
            break
      
'''
iterable_object = [1,2,3,4]
it = iter(iterable_object)
print(it)
print(next(it))#element print


name = "python"
it = iter(name)
print(next(it))

t = (1,2,3)
it = iter(t)
print(it)
#we can create objects with diff  types like list,
d ={"a":10,"b":20}
it = iter(d)
print(next(it))#in this it goes only to the keys

#Iterator No:
nums = [i for i in range(100000)]
#huge memory
#iterator approach
nums = iter(range(100000))
#only the current element will be procrssed

#creating a custom iterator
#Class is a key word

class Count:
    #constructor
    def __init__(self,limit):#self refer to the current object
        self.num = 1
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.num>self.limit:
            raise StopIteration
        x = self.num
        self.num +=1
        return x
#object creation
c = Count(5)
for i in c:
    print(i)

class even:
    def __init__(self,limit):
        self.num =2
        #max limit
        self.limit = limit
    def __iter__(self):#this method makes the object 
        #iterable it returns the iterator object itself
        return self
    def __next__(self):
        if self.num >self.limit:
            raise StopIteration
        x = self.num
        self.num  +=2
        return x
c = even(10)
for i in c:
    print(i)
        
    
    