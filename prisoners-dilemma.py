firstRound = True

global playerScore
global computerScore

global computerIsContent

playerScore = 0
computerScore = 0

round = 1

computerIsContent = True

global lastPlayerCooperate
lastPlayerCooperate = None

def tft():
	if firstRound:
		return True
	else:
		return lastPlayerCooperate

def grudger():
	if computerIsContent:
		return True
	else:
		return False



while round <= 10:
	playerChoice = input("Cooperate? (Y/N): ")
	if playerChoice == "y" or playerChoice == "Y":
		playerCooperate = True
	if playerChoice == "n" or playerChoice == "N":
		playerCooperate = False

	#change the function used to change behavior of the computer
	computerCooperate = tft()

	#calculate scores
	if playerCooperate and computerCooperate:
		playerScore += 3
		computerScore += 3
	if playerCooperate and not computerCooperate:
		playerScore += 0 #just for show
		computerScore += 5
	if not playerCooperate and computerCooperate:
		playerScore += 5
		computerScore += 0 #just for show
		computerIsContent = False
	if not playerCooperate and not computerCooperate:
		playerScore += 2
		computerScore += 2
		computerIsContent = False
	print("")
	print("You Cooperated: " + str(playerCooperate))
	print("Computer Cooperated: " + str(computerCooperate) + "\n")

	round += 1
	print("Player Score: " + str(playerScore))
	print("Computer Score: " + str(computerScore) + "\n")
	firstRound = False
	lastPlayerCooperate = playerCooperate

if playerScore > computerScore:
	print("You won by " + str(playerScore - computerScore) + " points.")
elif playerScore == computerScore:
	print("You tied with the computer.")
else:
	print("The computer beat you by " + str(computerScore - playerScore) + " points.")
