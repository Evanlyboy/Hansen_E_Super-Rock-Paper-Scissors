from random import randint
from gameComponents import winLose, gameVars

# works perfectly, don't fuck with this

# invoke function
def winner():
	# compare the two
	if gameVars.CPU == gameVars.player:
		# tie - nothing else to compare, so it'll exit
		print("A tie! Try again")

	elif gameVars.player == "rock":
		if gameVars.CPU == "paper":
			print("You lose")
			gameVars.playerLives = gameVars.playerLives -1
		else:
			print("You win!")
			gameVars.CPULives = gameVars.CPULives - 1

	elif gameVars.player == "paper":
		if gameVars.CPU == "scissors":
			print("You lose")
			gameVars.playerLives = gameVars.playerLives -1
		else:
			print("You win!")
			gameVars.CPULives = gameVars.CPULives - 1

	elif gameVars.player == "scissors":
		if gameVars.CPU == "rock":
			print("You lose!")
			gameVars.playerLives = gameVars.playerLives -1
		else:
			print("You win!")
			gameVars.CPULives = gameVars.CPULives - 1

	else:
		print("Missed input, try again")