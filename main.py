from random import randint
from gameComponents import winLose, gameVars, gameResult

# set up our game loop
while gameVars.player is False:
	gameVars.player = input("Choose your weapon: Rock, Paper, or Scissors: ")
	gameVars.CPU = gameVars.weapon[randint(0, 2)]

	if gameVars.player == "exit":
		exit();
	else:
		# confirming player input
		print("player chose: " + gameVars.player)
		print("the computer chose: " + gameVars.CPU)

		# haha I figured it out
		gameResult.winner()
		
		print("player lives :" + str(gameVars.playerLives))
		print("CPU lives: " + str(gameVars.CPULives))

		if gameVars.playerLives == 0:
			winLose.winorlose("Game over, kid. You're outta here")
		elif gameVars.CPULives == 0:
			winLose.winorlose("Supreme champion! You have bested 2000 years of technological achievement")
		else:
			gameVars.player = False
