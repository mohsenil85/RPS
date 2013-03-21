import mohseni_logan_element as e
import random
class Player:
	def __init__(self, _name):
		self._name = _name
	def name(self):
		return self._name
	def play(self):
		raise NotImplementedError("Not yet implemented")


class StupidBot(Player):
	"StupidBot"
	def play(self, Element):
		aRock = e.Rock('aRock')
		print(self.__doc__, "plays a", aRock.__doc__, "!")#i'm not sure if this
		#is a good idea or not, using the __doc__ fiedls .  But at least it was easy.
		return aRock.compareTo(Element)# I realize i should have just had one
	#method and not have had different play() and getPlayed() methods.  For some reason I thought it would be easier. But really it's just one extra level of abstraction to deal with.
	def getPlayed(self):
		print(self.__doc__, "plays a",  e.Rock.__doc__, "!")
		return e.Rock

class RandomBot(Player):
	"RandomBot"
	def play(self, Element):
		anElement = random.choice(e.moves)
		theElement = anElement('thing')
		print(self.__doc__, "plays a", theElement.__doc__, "!")
		return theElement.compareTo(Element)
	def getPlayed(self):
		anElement = random.choice(e.moves)
		theElement = anElement('thing')
		print(self.__doc__, "plays a", anElement.__doc__, "!")
		return anElement

class IterativeBot(Player):
	"IterativeBot"
	def __init__(self, _name, _index):
		self._name = _name
		self._index = _index
	def play(self, Element):
		self._index += 1
		self._index %= 4
		anElement = e.moves[self._index]
		theElement = anElement('thing')
		print(self.__doc__, "plays a", theElement.__doc__, "!")
		return theElement.compareTo(Element)
	def getPlayed(self):
		self._index += 1
		self._index %= 4
		print(self.__doc__, "plays a", e.moves[self._index].__doc__, "!")
		return e.moves[self._index]

class LastPlayBot(Player):
	"LastPlayBot"
	def __init__(self, _name, _play):
		self._name = _name
		self._play = _play
	def play (self, Element):
		anElement = self._play
		theElement = anElement('thing')
		print(self.__doc__, "plays a", theElement.__doc__, "!")
		self._play = Element
		return theElement.compareTo(Element)
	def getPlayed(self):
		print(self.__doc__, "plays a", self._play.__doc__, "!")
		return self._play

class MyBot(Player):
	"MyBot"
	def __init__(self, _play):
		self._play = _play
	def play (self, Element):
		self._play = Element
		anElement = Element
		theElement = anElement('thing')
		print(self.__doc__, "plays a", theElement.__doc__, "!")
		return theElement.compareTo(Element)
	def getPlayed(self):
		aRock = e.Rock('aRock')
		print(self.__doc__, "plays a", aRock.__doc__, "!")
		return aRock


class Human(Player):
	"Human"
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
		return e.moves[choice]
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
	"Human"
	def play(self, Element):
		print("You see a", Element.__doc__)
		print("Please choose:")
		choice = self.playInput()
		print(self.__doc__, "plays", e.moves[choice].__doc__)
		return e.moves[choice].compareTo(Element, Element)

	def getPlayed(self):
		print("You were attacked by", Element.__doc__)
		print("Please choose:")
		choice = self.playInput()
		print("You chose", e.moves[choice].__doc__)
		return e.moves[choice].compareTo(Element, Element)

bots = [StupidBot, RandomBot, IterativeBot, LastPlayBot, Human, MyBot] 
humans = [Human, AdventureMode]

