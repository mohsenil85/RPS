import element as e
import random
class Player:
	def __init__(self, _name):
		self._name = _name
	def name(self):
		return self._name
	def play(self):
		raise NotImplementedError("Not yet implemented")

class StupidBot(Player):
	def play(self, Element):
		aRock = e.Rock('aRock')
		return aRock.compareTo(Element)
	def getPlayed(self):
		return e.Rock

class lizBot(Player):
	def play(self, Element):
		lizard = e.Lizard('liz')
		return lizard.compareTo(Element)
	def getPlayed(self):
		return e.Lizard

class RandomBot(Player):
	def play(self, Element):
		anElement = random.choice(e.moves)
		theElement = anElement('thing')
		return theElement.compareTo(Element)
	def getPlayed(self):
		return random.choice(e.moves)

class IterativeBot(Player):
	def __init__(self, _name, _index):
		self._name = _name
		self._index = _index
	def play(self, Element):
		self._index += 1
		self._index %= 4
		anElement = e.moves[self._index]
		theElement = anElement('thing')
		return theElement.compareTo(Element)
	def getPlayed(self):
		self._index += 1
		self._index %= 4
		return e.moves[self._index]

class LastPlayBot(Player):
	def __init__(self, _name, _play):
		self._name = _name
		self._play = _play
	def play (self, Element):
		anElement = self._play
		theElement = anElement('thing')
		self._play = Element
		return theElement.compareTo(Element)
	def getPlayed(self):
		return self._play


class Human(Player):
	def play(self, Element):
		print("Please choose:")
		choice = self.playInput()
		print("You chose", e.moves[choice].__doc__)
		print("Your opponent chose", Element.__doc__)
		return e.moves[choice].compareTo(Element, Element)

	def getPlayed(self):
		print("Please choose:")
		choice = self.playInput()
		print("You chose", e.moves[choice].__doc__)
		return e.moves[choice].compareTo(Element, Element)
	def playInput(self):
		for i in range(e.moves.__len__()):
			print(i+1, e.moves[i].__doc__)
		notDone = True
		while (notDone):
			choice =  int(input("> "))
			if range(e.moves.__len__()).__contains__(choice - 1) :
				notDone = False
			else:
				print("Invalid choice") 
		return choice - 1
		
class AdventureMode(Human):
	def play(self, Element):
		print("You see a", Element.__doc__)
		print("Please choose:")
		choice = self.playInput()
		print("You chose", e.moves[choice].__doc__)
		return e.moves[choice].compareTo(Element, Element)

	def getPlayed(self):
		print("You were attacked by", Element.__doc__)
		print("Please choose:")
		choice = self.playInput()
		print("You chose", e.moves[choice].__doc__)
		return e.moves[choice].compareTo(Element, Element)
