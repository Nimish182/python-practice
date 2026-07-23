# #recursive function
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(8)


#wa recursive fun to print all elements in a list
def print_list(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)


marks=[85, 92, 78, 96, 88, 48]

print_list(marks)
