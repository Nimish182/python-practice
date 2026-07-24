class Account():
    def __init__(self):
        self.__balance=1000             # __balance here "__" is making this attribute private
    def Deposit(self,amt):
        self.__balance+=amt
    def get_balance(self):
        return self.__balance
account=Account()
account.Deposit(500)
print(account.get_balance())
    