'''
Login Authentication system:
A compny wants to store user credentials
write a program:
1.
'''
class System:
    def company(self):
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        try:
            with open("newfile.txt", "a") as file:
                file.write(username + " " + password + "\n")
            print("Registration successful")
        except Exception as e:
            print(e)
    def login(self):
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        found = False

        try:
            with open("newfile.txt", "r") as file:
                for line in file:
                    u, p = line.strip().split()

                    if username == u and password == p:
                        found = True
                        break

            if found:
                print("Login successful")
            else:
                print("Invalid credentials")

        except FileNotFoundError:
            print("No registered users found.")

obj = System()

obj.company()   # Register user
obj.login()     # Login user
    
        



