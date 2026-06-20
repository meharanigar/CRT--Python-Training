username = input("enter the username:")


#first condition

if username == "admin":
    password = input("enter the password:")

    #neasted condition
    if password == "1234":
        print("login is successful")
    else:
        print("wrong password")

else:
    print("invalid username")