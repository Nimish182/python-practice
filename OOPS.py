class Students:

    college_name= "PCCOE"
    # name="annonymous"       #here name is class attribute

    #default constructor
    # def __init__(self):
    #     pass
# the default constructor is gonna pass anyway as it doesn't have any parameter, function and task to perform.


#parameterized constructor
    def __init__(self,name,marks):   #here self=object (for example s1,s2 are objects)
                                     #here name is an object attribute.

        self.name=name          #self.name= instance attribute
        self.marks=marks
        # print("Adding new student in database")

    def welcome(self):
        print("welcome to the college, ", self.name)

    def get_marks(self):
        return self.marks       #here the function created get_marks is the method in OOPs
            

s1=Students("Nimish",6.6)
s1.welcome()
print(s1.get_marks())

# print(s1.name,s1.marks)                 #wondered why name is not "annonymous" bcoz is a class attribute
                                        #  obj attr > class attr .... the precedence of object attributes is always higher than the class attributes
# print(s1.college_name)

# s2=Students("Aryan", 6.9)
# print(s2.name,s2.marks)
# print(s2.college_name)
