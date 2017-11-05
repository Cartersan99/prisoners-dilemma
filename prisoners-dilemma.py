firstRound = True

global playerScore
global computerScore
playerScore = 0
computerScore = 0

round = 0

global lastPlayerCooperate
lastPlayerCooperate = None

def calculateComputerChoice(lastPlayerCooperate):
	if firstRound:
		return True
	else:
		return lastPlayerCooperate

while True:
	playerChoice = input("Cooperate? (Y/N): ")
	if playerChoice == "y" or playerChoice == "Y":
		playerCooperate = True
	if playerChoice == "n" or playerChoice == "N":
		playerCooperate = False

	computerCooperate = calculateComputerChoice(lastPlayerCooperate)

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
	if not playerCooperate and not computerCooperate:
		playerScore += 2
		computerScore += 2

	print("You Cooperated:" + str(playerCooperate))
	print("Computer Cooperated:" + str(computerCooperate))

	round += 1
	print(playerScore)
	print(computerScore)
	firstRound = False
	lastPlayerCooperate = playerCooperate
