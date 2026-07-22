tup=(1,4,9,16,25,36,49,64,81,100)
# for num in tup:
#     print(num)


#     #search no x in this tuple
x=(int(input("Enter a number to search in the tuple: ")))
idx=0
for el in tup:
    if el==x:
        print(" No fount at index", idx)
        break
    idx+=1
