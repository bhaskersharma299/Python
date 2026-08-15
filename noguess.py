import random
choice=str(input("Do you want to play a game ?\nPress Y for Yes and N for No!\n"))
attempt=0
if(choice=='Y' or choice=='y'):
    d=random.randint(1,1000)
    

    while True:
        n=int(input("Guess a No. from 1-1000 : "))
        attempt=attempt+1
        if(n>d):
            print("Too high !")
        elif(n<d):
            print("Too low!")
        else:
            print(f"Congratulations You Won . You guessed in {attempt} attempts!")
            break


elif(choice=='N' or choice=='n'):
    print("Thanks Come again!")

else:
    print("Invalid input!")

