
'''
task:
create a function bank_transaction
which accepts:
1.account holder
2.balance
3.transaction type(deposit/withdraw)
4.amount

use:
default arguments
return statement
'''
def bank_transaction(name="mehar"):
    balance = int(input("Enter the balance: "))
    transaction_type = input("Enter the type (deposit/withdrawal): ")

    if transaction_type == "deposit":
        deposit = int(input("Enter the amount: "))
        balance = balance + deposit
        print("Updated balance =", balance)

    elif transaction_type == "withdrawal":
        withdrawal = int(input("Enter the amount: "))

        if withdrawal > balance:
            print("Insufficient balance")
        else:
            balance = balance - withdrawal
            print("Updated balance =", balance)

    else:
        print("Invalid transaction type")

bank_transaction("mehar")