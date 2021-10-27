from random import randint

# instatiating the choices
weapon = ["rock", "paper", "scissors"]

player = False

playerLives = 5
CPULives = 5

# set up our game loop


def winorlose(status):
    print("you" + status)

    choice = input("do you want to play again? y/n: ")

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


while player is False:
	player = input("Choose your weapon: Rock, Paper, or Scissors: ")
	CPU = weapon[randint(0, 2)]

	# confirming player input
	print("player chose: " + player)
	print("the computer chose: " + CPU)

# compare the two
	if CPU == player:
		# tie - nothing else to compare, so it'll exit
		print("Tie! Try again")

	elif player == "rock":
		if CPU == "paper":
			print("you lose!")
			playerLives = playerLives -1
		else:
			print("you win!")
			CPULives = CPULives - 1

	elif player == "paper":
		if CPU == "scissors":
			print("you lose!")
			playerLives = playerLives -1
		else:
			print("you win!")
			CPULives = CPULives - 1

	elif player == "scissors":
		if CPU == "rock":
			print("you lose!")
			playerLives = playerLives -1
		else:
			print("you win!")
			CPULives = CPULives - 1

	print("player lives :" + str(playerLives))
	print("CPU lives: " + str(CPULives))

	if playerLives == 0:
		winorlose("lost")

	if CPULives == 0:
		winorlose("won")

	player = False
# print the outcome
