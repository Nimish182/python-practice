#  Create a new file practice.txt add following data in it
# Hi everyone
# we are learning file I/O
# using Java
# I like programming in Java
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\nusing Java\nI like programming in Java")


#WAF that replaces all occurences of "java" with "python" in above file
# with open("practice.txt", "r") as f:
#     data=f.read()
# new_data= data.replace("Java","python")   #Java and java are not same in python
# print(new_data)
# with open("practice.txt", "w") as f:
#     f.write(new_data)



# Search if word learning exist in your file or not
# word=("xlearning")
# with open("practice.txt", "r") as f:
#     data=f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")



#WAF to find in which line word learning is present first. print -1 if not found
# def check_for_line():
#     word="python"
#     data=True
#     line_no=1
#     with open("practice.txt", "r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print("found")
#                 return
#             line_no+=1

#     return -1   
# print(check_for_line())



#From a file containing numbers separated by comma, print the count of even numbers.
with open("practice.txt","r") as f:
    data=f.read()
    print(data)

