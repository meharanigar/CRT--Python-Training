def productivity_report(activities):
    #dict to store emplyoe task in count
    count = {}
    #traverse each activity
    for activity in activities:
        #jhon : Login-->name = Jhone
        name ,task = activity.split()
        name = name.lower()
        #check if employee
        #already exists in dict
        if name in count:
            count = count +1
        else:
             count[name]= 1
            
    employees = list(count.items())
    print(employees)
