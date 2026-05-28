import random

target=random.randint(1,50)

while True:
    userchoice=input("guess the target or quit")
    if(userchoice=="q"):
        break
    userchoice=int(userchoice)

    if(userchoice==target):
        print("you guessed the currect number !!!!,congradulations")


    elif(userchoice>target):
        print("guess of a smaller number")

    else:
        print("guess of a bigger number")




print("game over!!!!")       
    



