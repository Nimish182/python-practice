#reading a file
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print("data type of file is ",type(data))
# f.close()

#writing in a file
# w mode- this modes does complete overwirting bu deleting previous txt in the file
# f=open("demo.txt","w")
# f.write("I am having fun. /n My name is Nimish./n I love my life.")
# f.close()


# a mode= this mode will add data after the current data
# f=open("demo.txt","a")
# f.write("I am learning python.")
# f.close()


#WITH syntax
# with open("demo.txt") as f:
#     data=f.read()
#     print(data)


# with open("demo.txt", "w") as f:
#     f.write("\n my name is Nimish. \n I love batman.\n I am going to watch spiderman")




#DELETING a file
# import os
# os.remove("demo.txt")
