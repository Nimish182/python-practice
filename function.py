#Defining a function for calculating the sum of 2 nos
# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum

# calc_sum(2,3)
# calc_sum(10,15)



# #fun for average of 3 nos
# def average(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg


# average(10,20,30)


# average(50,100,150)

# average(98,97,95)





#WAP to print the length of a list(list is the parameter)
# cities=["Pune", "Mumbai", "Banglore", "Hyderabad", "Kolkata"]
# heroes=["Spiderman", "Superman", "Batman", "Ironman", "Captain america", "Thor", "Hulk"]
# flowers=["rose", "Lotus", "lily", "tulips", "daisy"]
# def Len_list(list):
#     print(len(list))

# Len_list(flowers)
# Len_list(cities)
# Len_list(heroes)





# WAF to print elements of a list in single line
cities=["Pune", "Mumbai", "Banglore", "Hyderabad", "Kolkata"]
heroes=["Spiderman", "Superman", "Batman", "Ironman", "Captain america", "Thor", "Hulk"]
flowers=["rose", "Lotus", "lily", "tulips", "daisy"]

# def print_list(list):
#     i=0
#     for i in range(0,len(list)):
#         print(list[i],end=" ")

# it could also be written as
def print_list(list):
    for item in list:
        print(item, end=" ")


print_list(cities)
print_list(heroes)
print_list(flowers)





#WAF to find factorial of n
# def fact_n(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# fact_n(3)





#WAF to convert USD to INR
# def converter(usd_val):
#     inr_val=usd_val*83
#     print(usd_val,"USD=",inr_val, "INR")


# converter(27)



#WAF to return if the input no. is even or odd
# def Even_Odd(n):
#     if(n%2==0):
#         print("Even")
#     else:
#         print("Odd")


# Even_Odd(5)
# Even_Odd(6)