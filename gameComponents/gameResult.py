from random import randint
from gameComponents import winLose, gameVars

# invoke function
def winner():
	# compare the two
	if gameVars.CPU == gameVars.player:
		# tie - nothing else to compare, so it'll exit
		print("Tie! Try again")

	elif gameVars.player == "rock":
		if gameVars.CPU == "paper":
			print("you lose!")
			gameVars.playerLives = gameVars.playerLives -1
		else:
			print("you win!")
			gameVars.CPULives = gameVars.CPULives - 1

	elif gameVars.player == "paper":
		if gameVars.CPU == "scissors":
			print("you lose!")
			gameVars.playerLives = gameVars.playerLives -1
		else:
			print("you win!")
			gameVars.CPULives = gameVars.CPULives - 1

	elif gameVars.player == "scissors":
		if gameVars.CPU == "rock":
			print("you lose!")
			gameVars.playerLives = gameVars.playerLives -1
		else:
			print("you win!")
			gameVars.CPULives = gameVars.CPULives - 1
			