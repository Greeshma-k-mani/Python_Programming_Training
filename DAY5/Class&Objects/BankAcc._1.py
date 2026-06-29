class BankAccount:
    #Constructor
    def __init__(self,balance,name):
        self.name=name
        self.__balance=balance
    # Getters
    def get_balance(self):
        return self.__balance   
    # Setters
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Invalid balance amount")
     

#Main
account=BankAccount(500,"BAVITH")
print(account.get_balance())
account.set_balance(500)
print("Total after setting balance",account.get_balance())

