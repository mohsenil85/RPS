import mohseni_logan_element as e
import mohseni_logan_players as p

def getInput(size):
	notDone = True
	while (notDone):
		choice = int(input("> "))
		if not range(size).__contains__(choice - 1):
			print("Invalid Input")
		else:
			notDone = False
			return (choice - 1)
def printMenu():
	for i in range(p.bots.__len__()):
		print(i+1, p.bots[i].__doc__)
def round(p1, p2):
	return  p1.play(p2.getPlayed())

def getBot(index):
	if index == 2:
		return p.IterativeBot('itrBot', 1)
	elif index == 3:
		return p.LastPlayBot('lastPlayBot', e.Rock)
	elif index == 5:
		return p.MyBot( e.Rock)
		
	else:
		return p.bots[index]('Player')
	

def main():
	print("Welcome to Rock Paper Scissors Lizard Spock")
	print("Logan Mohseni, -01449701")
	print()
	print("Please choose the first player:")
	printMenu()
	print()
	choice = getInput(p.bots.__len__())
	player1 = getBot(choice)
	print("Player 1 is a", player1.__doc__)
	print()
	print("Please choose the second player:")
	printMenu()
	print()
	choice = getInput(p.bots.__len__())
	while (choice == 5):
		print("AlwaysTries is not implemented for the direct object case!")
		print("Please pick something else.")
		choice = getInput(p.bots.__len__())
	player2 = getBot(choice)
	print("Player 2 is a", player2.__doc__)

	print()
	p1Score = 0
	p2Score = 0
	for i in range(5):
		result = round(player1, player2)
		print(result[1])
		score = result[0]
		if score == 'Win':
			print("Player 1 wins!")
			p1Score += 1
		elif score == 'Lose':
			print("Player 2 wins!")
			p2Score += 1
		else:
			print("Tie")
		print()
	print("Score was ", p1Score, "to", p2Score)
	if p1Score > p2Score:
		print("Player 1 wins.")
	elif p1Score < p2Score:
		print("Player 2 wins.")
	else:
		print("Game was a draw")
	


if  __name__ =='__main__':
	    main()
