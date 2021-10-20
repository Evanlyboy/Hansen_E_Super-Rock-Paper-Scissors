from random import randint

# player will be the weapon the player chooses via input
player = input("Choose your weapon: Rock, Paper, or Scissors: ")

#instatiating the choices
weapon = ["rock", "paper", "scissors"]

#make the ai choose
CPU = weapon[randint(0, 2)]

#confirming player input
print("player chose: " + player)
print("the computer chose: " + CPU)

#compare the two
if (CPU == player):
	# tie - nothing else to compare, so it'll exit
	print("Tie! Try again")
elif (player == "rock"):
	if (CPU == "paper"):
		print("you lose!")
	else:
		print("you win!")
elif (player == "paper"):
	if (CPU == "scissors"):
		print("you lose!")
	else:
		print("you win!")
elif (player == "scissors"):
	if (CPU == "rock"):
		print("you lose!")
	else:
		print("you win!")
#choose the winner

#print the outcome