# Single Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started.....")

#     @staticmethod
#     def stop():
#         print("car stopped....")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# car1=ToyotaCar("Fortuner")
# car2=ToyotaCar("Prius")

# print(car1.name)



# Multi Level Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started.....")

#     @staticmethod
#     def stop():
#         print("car stopped....")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self, brand):
#         self.type=type

# car1= Fortuner("diesel")
# car1.start()




# Multiple Inheritance
# class A:
#     varA="Welcome to class A"
# class B:
#     varB="Welcome to class B"
# class C(A,B):
#     varC="Welcome to class C"

# c1=C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)




# Super Method
# class Car:
#     def __init__(self,type):
#         self.type=type
#         pass
#     @staticmethod
#     def start():
#         print("car started.....")

#     @staticmethod
#     def stop():
#         print("car stopped....")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         self.name=name
#         super().__init__(type)
#         super().start()

# car1= ToyotaCar("prius","electric")
# print(car1.type)


# Class Method
class Person:
    name="annonymous"

    # def changeName(self,name):
    #     Person.name=name

    #instead of above commented lines we can use Class Methods
    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("Nimish")
print(p1.name)
print(Person.name)