'''
what is dict?
collection of key value pairs

key: value
a8 :"mehar"
dict = {}
dictionary is mutable and also immutable
becasuce: it have keys = keys are immutable and values are mutable
dictionary not allows duplicates of---key  but values can be duplicate


@it have no fixed indexing
@searching is very efficient:O(1)
@dictionary uses hashing techinque to search hence:O(1)


creation of dictionary: method--1
student = {
         "name":"mehar",
         "roll.no":08,
         "age":20
}


why we use dictionary?
1.lables
2.properties
3.mapping the relationships
--->we cant sort the dictonary in directly  we use "key"  variable

'''
student = {
         "name":"mehar",
         "roll.no":"a8",
         "age":20
}
print(student)

#second method to creating the dictionary:

student = dict(name = "nigar", age = 20 , branch = 'ai')
print(student)

#3rd method: empty dict
data ={}
print(data)

#we can access data with keys
'''
feature             list                dict
ordered             yes                  no
access(indexing)    yes                  keys no
arr[0]              yes                  student["keys"]
'''
employee={}
employee["name"] = "mehar"
employee["age"] = 19
#update the value
employee["age"] = 20
#deleting the value
employee.pop("age")
print(employee)
#2nd method 
del student["roll.no"]
print(student)

'''
dictionary methods:
#keys() --> returns the keys 
print(student.keys())

#values() ---> returns all the values 
print(student.values())

#Items() ---> returns all the values in the dictionary 
print(student.items())
print(student["branch"])--->gives error
'''

#access the elements
print(student.get("branch"))
#cause better to use the get method -- if elements are not in the dict it gives none instead of error


#update method will give the flexibility to add multible elements at a time
student.update({"branch":"ai","college":"chalapathi","age":20})
print(student)

# popitem: remove the last  inserted pair
student.popitem()
print(student)

#looping on dictionary
for i in student:
    print(i)

#iterating on values:
for value in student.values():
    print(value)

#for keys and values ew use
for keys,value in student.items():
    print(keys,value)


#nested dict: dict inside dict
student = {

    "s1" :{
        "name":"nigar",
        "age":20    },
    "s2":{
        "name":"nigar",
        "branch":"ai"
    }
    
}
print(student["s1"]["name"])

#can i store list inside the dict?
student = {

    "name":"darshan",
    "mark":[20,35,67,80]
}
print(student)

# yes we can store multiple dictionarys in list
m = [

    {"name":"taslim","roll.no":23},
    {"name":"nigar","roll.no":34}
    
]
student[0]["name"]

#dict comprehension

#{key:values for variables in iterable}
squares = {x:x*x for x in range(1,11)}
print(squares)

#keys: rules
'''
int
string
list --- no
dictionary

student = {
    1:"Manish",
    "Roll":08,
    (1,2):"tuple"
    [1,2,3]:"List" # List is not be used as a key 
    {"Name":"Manish"}:"Hello" #cant use 
}'''