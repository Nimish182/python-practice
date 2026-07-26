import random
target= random.randint(1,100)
while True:
    userCHoice = int(input("Guess the target no. or Quit(Q): "))
    if(userCHoice=="Q"):
        break
    if (userCHoice==target):
        print("Success: Correct Guess!!")
        break
    elif(userCHoice<target):
        print("your no. was too small. Take a bigger guess")
    else:
        print("your no. was too big. Take a smaller guess")

print("-------GAME OVER-------")

