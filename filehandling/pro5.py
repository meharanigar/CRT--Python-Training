# '''
# A company stores server logs in a file
# write apython program
# 1.Read log.txt
# then count
# total lines
# error msg
# warning msg
# info msg
# display analasis report

# '''
class Server:
    def company(self):
        try:
            # Writing into file
            with open("login.txt", "w") as file:
                file.write("some error in the code\n")
                file.write("systems gives warning msg\n")
                file.write("enter some info about you\n")

            # Reading the file
            with open("login.txt", "r") as file:
                lines = file.readlines()

            error = 0
            warning = 0
            info = 0

            for line in lines:
                if "error" in line:
                    error += 1
                elif "warning" in line:
                    warning += 1
                elif "info" in line:
                    info += 1

            print("Log Report")
            print("Total lines:", len(lines))
            print("Errors:", error)
            print("Warnings:", warning)
            print("Info:", info)

        except FileNotFoundError as e:
            print(e)

obj = Server()
obj.company()

class Credentials:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

        try:
            with open("user.txt", "a") as file:
                file.write(user_name + " " + password + "\n")
            print("Registration Successful")
        except Exception as e:
            print(e)

    def login(self):
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        found = False

        try:
            with open("user.txt", "r") as file:
                for line in file:
                    u, p = line.strip().split()

                    if username == u and password == p:
                        found = True
                        break

            if found:
                print("Login Successful")
            else:
                print("Login Failed")

        except Exception as e:
            print(e)


obj = Credentials("Meher", "1234")
obj.login()