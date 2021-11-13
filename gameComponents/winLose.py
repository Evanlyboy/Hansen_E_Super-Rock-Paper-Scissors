from gameComponents import gameVars

def winorlose(status):
    print(status)
    print("--------------------------")
    badInput = True

    while badInput == True:
        # ask them the big question
        choice = input("Do you want to play again? y/n: ")
        # if no, exit
        if choice == "n":
            print("================== Smell ya later ==================")
            exit()
        elif choice == "y":
            #fuck global variables, all my homies hate global variables
            gameVars.CPULives = 3
            gameVars.playerLives = 3
            gameVars.player = False
            badInput = False
        else:
            #the catch for anything that isn't y or n
            print("Bad input, try just y or n")
            badInput = True

# holy shit fucking finally it's working