import element as e
import players as p

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
	print(p1.__doc__)
	print(p1.play(p2.getPlayed()))


def main():
	print("Welcome to Rock Paper Scissors Lizard Spock")
	print("Logan Mohseni, -01449701")
	print("Please choose the first player:")
	printMenu()
	player1 = p.bots[getInput(p.bots.__len__())]('Player1')
	print("Player 1 is a", player1.__doc__)
	print("Please choose the second player:")
	printMenu()
	player2 = p.bots[getInput(p.bots.__len__())]('Player2')
	print("Player 2 is a", player1.__doc__)
	round(player1, player2)

if  __name__ =='__main__':
	    main()
