# a= int(input("Enter the no.: "))
# b= int(input("Enter the no.: "))
# c= int(input("Enter the no.: "))
# if(a>b and a>c):
#     print("a is greater")
# elif(b>c):
#     print("b is greater")
# else:
#     print("c is greater")



#Greatest of 4 nos
a= int(input("Enter the 1st no.: "))
b= int(input("Enter the 2nd no.: "))
c= int(input("Enter the 3rd no.: "))
d= int(input("Enter the 4th no.: "))
if(a>b and a>c and a>d):
    print("a is greatest")
elif(b>c and b>d):
    print("b is the greatest")
elif(c>d):
    print("c is greatest")
else:
    print("d is greatest")