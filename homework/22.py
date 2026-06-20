#task:2
class Inventory:
    def __init__(self):
        self.lst = [10, 30, 50]
    def purchase(self, index, quantity):
        try:
            if index < 0 or index >= len(self.lst):
                raise Exception("InvalidProductIndexError")
            if quantity <= 0:
                raise Exception("InvalidQuantityError")
            if quantity > self.lst[index]:
                raise Exception("OutOfStockError")
            self.lst[index] -= quantity

            print("Purchase Successful")
            print("Remaining Stock:", self.lst)
        except Exception as e:
            print(e)
obj = Inventory()
index = int(input("Enter index: "))
quantity = int(input("Enter quantity: "))
obj.purchase(index, quantity)