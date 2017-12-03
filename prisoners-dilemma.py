import random

firstRound = True

global p1Score
global p2Score

p1Score = 0
p2Score = 0

global grudgerIsContent

round = 1

grudgerIsContent = True

global lastp1Cooperate
lastp1Cooperate = None

global lastp2Cooperate
lastp2Cooperate = None

#each function outputs cooperate as True and not cooperate as False
def allcooperate():
	return True

def allnotcooperate():
	return False

def rand():
	return bool(random.getrandbits(1))

def player():
	while True:
		playerChoice = input("Cooperate? (Y/N): ")
		if playerChoice.lower() == "y" or playerChoice.lower() == "yes":
			return True
		if playerChoice.lower() == "n" or playerChoice.lower() == "no":
			return False
		else:
			print("Not a valid answer.\n")
			continue

def grudger():
	if grudgerIsContent:
		return True
	else:
		return False

def tft():
	if firstRound:
		return True
	else:
		if playermap["p2"] == "tft":
			return lastp1Cooperate
		else:
			return lastp2Cooperate


def oppositetft():
	if firstRound:
		return False
	else:
		if playermap["p2"] == "tft":
			return not lastp1Cooperate
		else:
			return not lastp2Cooperate


# Full list of strategies (input them like this)
# "p1": tft,
# "p2": player
# replace tft and player with the strategies you want to use

# grudger
# rand
# player
# tft
# allcooperate
# allnotcooperate
# oppositetft

strats = [grudger, rand, player, tft, allcooperate, allnotcooperate, oppositetft]

playermap = {

	"p1": rand,
	"p2": rand

}

while round <= 10:

	#change the function used to change behavior of player1


	p1Cooperate = playermap["p1"]()

	
	#change the function used to change behavior of player2
	p2Cooperate = playermap["p2"]()

	#calculate scores
	if p1Cooperate and p2Cooperate:
		p1Score += 3
		p2Score += 3
	elif p1Cooperate and not p2Cooperate:
		p1Score += 0 #just for show
		p2Score += 5
		if playermap["p1"] == grudger:
			grudgerIsContent = False
	elif not p1Cooperate and p2Cooperate:
		p1Score += 5
		p2Score += 0 #just for show
		if playermap["p2"] == grudger:
			grudgerIsContent = False
	elif not p1Cooperate and not p2Cooperate:
		p1Score += 2
		p2Score += 2

	print("")
	print(playermap["p1"].__name__.title() + " (p1) Cooperated: " + str(p1Cooperate))
	print(playermap["p2"].__name__.title() + " (p2) Cooperated: " + str(p2Cooperate) + "\n")

	round += 1
	print(playermap["p1"].__name__.title() + " (p1) Score: " + str(p1Score))
	print(playermap["p2"].__name__.title() + " (p2) Score: " + str(p2Score) + "\n")

	firstRound = False

	lastp1Cooperate = p1Cooperate
	lastp2Cooperate = p2Cooperate

if p1Score > p2Score:
	print(playermap["p1"].__name__.title() + " (p1) won by " + str(p1Score - p2Score) + " points.")
elif p1Score == p2Score:
	print(playermap["p1"].__name__.title() + " (p1) tied with " + playermap["p2"].__name__)
else:
	print(playermap["p2"].__name__.title() + " (p2) won by " + str(p2Score - p1Score) + " points.")
