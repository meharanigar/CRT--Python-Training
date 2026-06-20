#login system
class LoginSystem:

    def __init__(self):
        self.users = ["admin", "john", "kavya", "mehar"]
    def login(self, username):
        if len(username) < 4:
            raise Exception("ShortUsernameError")
        if not username.isalpha():
            raise Exception("InvalidUsernameError")
        found = False
        for user in self.users:
            if user.lower() == username.lower():
                found = True
                break
        if not found:
            raise Exception("UserNotFoundError")

        print("Login Successful")
obj = LoginSystem()
try:
    uname = input("Enter Username: ")
    obj.login(uname)
except Exception as e:
    print(e)