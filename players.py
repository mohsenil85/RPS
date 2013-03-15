import element as e
class Player:
	def __init__(self, _name):
		self._name = _name
	def name(self):
		return self._name
	def play(self):
		raise NotImplementedError("Not yet implemented")

aRock = e.Rock('aRock')
class StupidBot(Player):
	def play(self, Element):
		return aRock.compareTo(Element)

class RandomBot(Player):
	def play(self, Element):
