# Create student class that takes name and marks of 3 subjects as a argument in the constructor. Then create a method to print average


# class Students():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def average(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi ",self.name,"your score average is ",sum/3)

# s1=Students("Nimish",[90,96,89])
# s1.average()



#Create account class with 2 attribute: balance and account no.
# Create methods for debit credit and printing the balance


# class Account():
#     def __init__(self,balance,acc_no):
#         self.balance=balance
#         self.acc_no=acc_no

#     def debit(self):
#         x=int(100)
#         debited=self.balance-x
#         print(debited,"has been debited from your bank account")

#     def credit(self):
#         x=int(100)
#         credited=self.balance+x
#         print(credited, "has been credited to your bank account")

#     def Print_balance(self):
#         print("You have ",self.balance, " in your account")

# c1=Account(1000,123123)

# c1.Print_balance()
# c1.debit()
# c1.credit()



class Account():
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount):
        self.balance-=amount
        print(amount,"has been debited from your bank account")
        print("total balance= ", self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print(amount, "has been credited to your bank account")
        print("total balance= ", self.get_balance())

    def get_balance(self):
        return self.balance

c1=Account(10000,123123)

c1.get_balance()
c1.debit(499)
c1.credit(500)
c1.credit(40000)

