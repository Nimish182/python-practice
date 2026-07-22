# # # Print nos from 1 to 100 and reverse order from 100 to 1 using while loop
# # i=100
# # while i>=1:
# #     print(i)
# #     i-=1



# #print multiplication table of a no n
# # n=int(input("Enter a no."))
# # i=1
# # while i<=10:
# #     print(i*n)
# #     i+=1



# #print the elements of a list using while loop
# # [1,4,9,16,25,36,49,64,81,100]

# list=[1,4,9,16,25,36,49,64,81,100]
# # i=0
# while i<len(list):
#     print(list[i])
#     i+=1




#Search for a no. x in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100)
i=0
x=int(input("Enter a no. to search: "))
while i<len(tup):
    if tup[i]==x:
        print("Found")
        break
    i+=1
else:
    print("Not Found")