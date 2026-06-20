#Decision making ability 
#Control flow decision
#1. how many times to execute  what to execute

# human analogy:
'''
if it rains ---> take umbrella
if marks > 40 ---> pass
if password correct --> login

'''

#program also need dcision making ability
#conteol flow:
#which statement to execute and in what order

'''
3-type of control flow
1.secquential:top to bottom execution
2.conditional:decision making
3.Looping:Rapetation

'''

# syntax:
#if --> to check the  condition:


#example:
age = 21
if age > 20:
    print("eligible")

    '''
    execution flow
            condition true?
            ececution the block

    '''



x = 10

if x>5:
        
        print("hello")
        

    #if:
    #    statement
    #else:
    #     statement



num = int(input("enter the number"))

if num % 2 == 0:
      print("even")
else:
      print("odd")    
  



'''
  execution flow
                                      condition ?
                                      /       \
                                    True      False
                                      |         |
                                    even       odd               
            
  '''

#elif ladder
#multiple conditions: miltiple decitions


#       #Syntax:
# if condition:
#       statement-1
# elif condition-2:
#       statement
# else:
#       statement



#task: build the student grading system

student = int(input("enter the name"))

if student > 90:
      print("A")

elif student < 80:
      print("B")

else:
      print("C")




      
