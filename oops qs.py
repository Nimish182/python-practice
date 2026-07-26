# Define a Circle class to create a circle with radius r using the constructor
# define an Area() method of the class which calculates the area of circle
# define a perimeter() method of the class which allows you to calculate the perimeter of cirle

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return (22/7)*self.radius**2

#     def perimeter(self):
#         return 2*(22/7)*self.radius

# c1=Circle(21)
# print(c1.area())
# print(c1.perimeter())




#Define and employee class with attribute role, deprtment and salary. This class also has a showDetails() method
#Create an engineer class that inherits properties from employee and has additional attributes: name and age


# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def showDetails(self):
#         print("role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer", "IT", "75000")

# # e1= Employee("accountant","Finance","60000")
# # e1.showDetails()

# e2= Engineer("Nimish",40,)
# e2.showDetails()


# Create a class Order ehich stores item and its price.print
# Use dunder function __gt__() to convoy that:
# order1 > order2 if price of order 1>price of order2



class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price


    def __gt__(self,order2):
        return self.price > self.order2

ord1=Order("Chips",20)
ord=Order("Tea",15)


print(ord1>ord2)  #True

