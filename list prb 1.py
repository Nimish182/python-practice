# WAP ask user to enter the names of 3 movies and store them in a list. Then print the list.

movie=[]
mov1=input("Enter the name of 1st movie: ")
mov2=input("Enter the name of 2nd movie: ")
mov3=input("Enter the name of 3rd movie: ")
# movie=[mov1,mov2,mov3]
movie.append(mov1)
movie.append(mov2)
movie.append(mov3)

print(movie)