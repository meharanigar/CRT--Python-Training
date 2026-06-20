class SheIsNotInHome(Exception):
    pass
check = input("checking if she is inside the home")
if check.lower() == "no":
    raise SheIsNotInHome("not there")
print("she is there")

#Login system:
class LoginSystem:
    def login (self,username,password):
        try:
            if username !="admin":
                raise ValueError("Invalid username")
            if password != "admin123":
                raise ValueError("invalid password")
            print("login successful")
        except ValueError as e:
            print("Error:",e)
oje = LoginSystem()
username = input("enter the username:")
password = input("enter the password")
oje.login(username,password)


#task:ATM
'''
Question:
Accept account balance and withdrawal amount. Raise exceptions if:
Withdrawal amount is negative.
Withdrawal amount exceeds balance.
Withdrawal amount exceeds daily limit of 25000.
Display remaining balance if transaction is successful

'''
class Account:

    def withdraw(self, balance, amount):
        try:
            if amount < 0:
                raise ValueError("Withdrawal amount is negative")

            if amount > balance:
                raise ValueError("Withdrawal amount exceeds balance")

            if amount > 25000:
                raise ValueError("Withdrawal amount exceeds daily limit of 25000")

            balance = balance - amount
            print("Transaction Successful")
            print("Remaining Balance:", balance)

        except ValueError as e:
            print("Error:", e)


acc = Account()

balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

acc.withdraw(balance, amount)


#task 2:
'''
A university wants to automate students results proce

class Univercity:
    def five_subject(self,marks):
        try:
            if marks < 0 or marks > 100:
                raise ValueError("negative and exceed values")
            if marks != int:
                raise ValueError("enter integers only")
            if  
'''
class InvalidMarksError(Exception):
    pass
class Student:
    def __init__(self):
        self.marks = []
    def input_marks(self):
        try:
            for i in range(5):
                mark = int(input(f"Enter subject{i+1}marks"))
            if mark < 0 or mark > 100:
                raise InvalidMarksError("Marks sholud be positive number")
            self.marks.append(mark)
            average = sum(self.marks)/5
            print("Average:",average)
            if average >= 75:
                print("Distinction")
            elif average >= 65:
                print("First class")
            elif average >=40:
                print("pass")
            else:
                print("fail")
        except ValueError:
            print("only numericals are allowed")
        except InvalidMarksError as e:
            print(e)
obj = Student()
obj.input_marks()