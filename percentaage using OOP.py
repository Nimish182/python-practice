# use of property decorator
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

    # def CalcPer(self):
        # self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

# instead of above method we use we can use property decorator
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

std1=Student(98,97,96)
print(std1.percentage)


std1.phy=86
print(std1.phy)
print(std1.percentage)