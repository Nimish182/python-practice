# # # # # # Store the following words meaning in the dictionary
# # # # # table = "a piece of furniture", "list of facts &figures"
# # # # # cat="a small animal"


# # # # dict={
# # # #      "cat": "a small animal",
# # # #     "table":["a piece of furniture", "list of facts & figures"],
# # # # }

# # # # print(dict)



# # # #You are given list of subjects for students. Assume 1 classroom is required for 1 subject. How many classrooms are needed by all students?
# # # # "python", "java", "c++", "python", "javascript","java", "python", "java", "c++", "c"

# # # subjects=["python", "java", "c++", "python", "javascript","java", "python", "java", "c++", "c"]
# # # print(len(set(subjects)))




# # # WAP to enter marks of 3 subjects from the user and store them in dictionary. Start with a empty dictionary and add one by one. Use subject name as key and marks as value
# # dict={}
# # # dict["python"] = float(input("enter the marks for python: "))
# # # dict["java"] = float(input("enter the marks for java: "))
# # # dict["c++"] = float(input("enter the marks for c++: "))

# # x=int(input("enter phy: "))
# # dict.update({"phy":x})

# # x=int(input("enter chem: "))
# # dict.update({"chem":x})

# # x=int(input("enter mat: "))
# # dict.update({"mat":x})

# # print(dict)






# #figure out a way to store 9 and 9.0 as a seperate valure in a set.(you can take help of built in data types)

# set={
# ("int",9),
# ("float",9.0)
# }
# # set={9,"9.0"}  #is 9.0 is a string, we can store it 
# print(set)





# n=int(input())
# if 1<=n<=100:
#     if(n%2==1):
#         print("Weird")
#     elif(n%2==0 and 2<=n<=5):
#         print("Not Weird")
#     elif(n%2==0 and 6<=n<=20):
#         print("Weird")
#     else:
#         print("Not Weird")






# a=int(input())
# b=int(input())
# # if (1<=a<=10^10):
# #     if (1<=a<=10^10):
# print(a+b)
# print(a-b)
# print(a*b)