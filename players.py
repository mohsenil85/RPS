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

class RandomBot(Player):
	def play(self, Element):
		anElement = random.choice(e.moves)
		theElement = anElement('thing')
		return theElement.compareTo(Element)

class IterativeBot(Player):
	def __init__(self, _name, _index):
		self._name = _name
		self._index = _index
	def play(self, Element):
		anElement = e.moves[self._index]
		theElement = anElement('thing')
		self._index += 1
		self._index %= 4
		return theElement.compareTo(Element)

