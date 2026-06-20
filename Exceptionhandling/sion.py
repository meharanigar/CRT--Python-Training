class StockUnailableError(Exception):
    pass
class PyamentFaildError(Exception):
    pass
class AddressError(Exception):
    pass
class Shop:
    def __init__(self,stock,address,payment):
        self.stock = stock
        self.address = address
        self.payment = payment
    def place_order(self):
        try:
            if self.stock <=0:
                raise StockUnailableError("product is outofstock")
            if not self.payment:
                raise PyamentFaildError("payment is faild")
            if self.address.strip() == "":
                raise AddressError("invalid address")
            print("order placed success")
        except StockUnailableError as e:
            print(e)
        except PyamentFaildError as e:
            print(e)
        except AddressError as e:
            print(e)
stock = int(input("enter the stock"))
payment_status = input("payment successful (yes/no)").lower()
address = input("enter the addres")
payment = payment_status == "yes"
obj = Shop(stock,address,payment)
obj.place_order()


#task:3
'''
1.accept filename from user
handle:
1.file not found
2.permission denied
3.empty file
Display:
number of lines :len(file,)
number of words
'''
class EmptyFileError:
    pass
class FileAnalyzer:
    def analyze(self,filename):
        try:
            file = open(filename)
            content = file.read()

            if content.strip() == "":
                raise EmptyFileError("file is empty")
            lines = len(content.splitlines())
            words = len(content.split())
            characters = len(content)
            #display the outputs
            print("Lines :",lines)
            print("words:",words)
            print("charecters:",characters)
            file.close()
        except PermissionError as e:
            print(e)
        except EmptyFileError as e:
            print(e)
        finally:
            print("analysis completed")
filename = input("enter the filename")
obj = FileAnalyzer()
obj.analyze(filename)