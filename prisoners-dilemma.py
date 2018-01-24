import random

firstRound = True # set this to true, will change it back to false after run

global p1Score, p2Score, roundnumber
p1Score, p2Score, roundnumber = 0,0,1

global grudgerIsContent
grudgerIsContent = True

global lastplayerCooperate
lastplayerCooperate = None

global lastp2Cooperate
lastp2Cooperate = None

global playerCooperateList
playerCooperateList = []

#each function outputs cooperate as True and not cooperate as False
def allcooperate():
	return True

def allnotcooperate():
	return False

def rand():
	#returns a random boolean (t/f)
	return bool(random.getrandbits(1))

def player():
	#interperets player input
	while True:
		playerChoice = input("Cooperate? (Y/N): ")
		if playerChoice.lower() == "pvp":
			playermap["p2"] = player
			continue
		if playerChoice.lower() == "y" or playerChoice.lower() == "yes":
			return True
		if playerChoice.lower() == "n" or playerChoice.lower() == "no":
			return False
		else:
			print("Not a valid answer.\n")
			continue

def grudger():
	#uses variable grudgerIsContent
	if grudgerIsContent:
		return True
	else:
		return False

def tft():
	#uses variable lastplayerCooperate
	if firstRound:
		return True
	else:
		return playerCooperateList[-1]


def oppositetft():
	if firstRound:
		return False
	else:
		return not playerCooperateList[-1]


# Full list of strategies (input them like this)
# "p1": tft,
# "p2": player
# replace tft and player with the strategies you want to use

# grudger - always cooperates until the other player does not cooperate, after that it will never cooperate again
# rand - random, like a coin toss.
# player - allows the user to input moves as Y or N
# tft - Cooperates on the first round, then follows the other player's last move.
# allcooperate - always cooperates.
# allnotcooperate - never cooperates.
# oppositetft - Does not cooperate on the first round, then does the opposite of the other player's last move.

strats = [grudger, rand, player, tft, allcooperate, allnotcooperate, oppositetft]

#change the functions used to change behavior of player1 and player2

playermap = {

	"p1": player,
	"p2": random.choice(strats)

}

while playermap["p2"] == player:
	playermap["p2"] = random.choice(strats)

while roundnumber <= 10:
	p1Cooperate = playermap["p1"]() #find the function name of p1 in playermap, call it
	p2Cooperate = playermap["p2"]() #find the function name of p1 in playermap, call it

	#CALCULATE SCORES
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

	#Print cooperate/not cooperate for each player
	print("")
	print("(p1) Cooperated: " + str(p1Cooperate))
	print("(p2) Cooperated: " + str(p2Cooperate) + "\n")

	print("(p1) Score: " + str(p1Score))
	print("(p2) Score: " + str(p2Score) + "\n")

	roundnumber += 1 #next round
	firstRound = False #first round over, used for strategies like tft, oppositetft, and grudger

	playerCooperateList.append(p1Cooperate) #add the player's moves to the list



#Determine the winner
if p1Score > p2Score:
	print("(p1) won by " + str(p1Score - p2Score) + " points.")
elif p1Score == p2Score:
	print("(p1) tied with " + playermap["p2"].__name__ + " (p2)")
else:
	print("(p2) won by " + str(p2Score - p1Score) + " points.")

#Tell them who they played against, wont really matter if computer player was chosen
print("You played against " + str(playermap["p2"].__name__) + ".")
