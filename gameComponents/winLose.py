from gameComponents import gameVars

def winorlose(status):
    print(status)

    choice = input("Do you want to play again? y/n: ")

    global playerLives
    global CPULives
    global player

    if choice == "n":
    	print("================== see ya! (loser) ==================")
    	exit()
    elif choice == "y":
    	CPULives = 5
    	playerLives = 5
    	player = False