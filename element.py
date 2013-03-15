class Element:
	def __init__(self, _name):
		self._name = _name

	def name(self):
		return self._name

	def compareTo(self, Element):
		raise NotImplementedError("Not yet implemented")

class Rock(Element):
	def compareTo(self, Element):
		if Element == Rock:
			return "Tie", "Rock equals Rock"
		elif Element == Paper:
			return "Lose", "Paper covers Rock"
		elif Element == Spock:
			return "Lose", "Spock vaporizes Rock"
		elif Element == Scissors:
			return "Win", "Rock crushes Scissors"
		elif Element == Lizard:
			return "Win", "Rock crushes Lizard"
		else:
			raise NotImplementedError("Not yet implemented")

class Scissors(Element):
	def compareTo(self, Element):
		if Element == Scissors:
			return "Tie", "Scissors equals Scissors"
		elif Element == Paper:
			return "Win", "Scissors cuts Paper"
		elif Element == Spock:
			return "Lose", "Spock smashes Scissors"
		elif Element == Rock:
			return "Lose", "Rock crushes Scissors"
		elif Element == Lizard:
			return "Win", "Scissors decapitate Lizard"
		else:
			raise NotImplementedError("Not yet implemented")
		
class Paper(Element):
	def compareTo(self, Element):
		if Element == Paper:
			return "Tie", "Paper equals Paper"
		elif Element == Rock:
			return "Win", "Paper covers Rock"
		elif Element == Spock:
			return "Win", "Paper disproves Spock"
		elif Element == Scissors:
			return "Lose", "Scissors cuts Paper"
		elif Element == Lizard:
			return "Lose", "Lizard eats Paper"
		else:
			raise NotImplementedError("Not yet implemented")

class Spock(Element):
	def compareTo(self, Element):
		if Element == Paper:
			return "Lose", "Paper disproves Spock"
		elif Element == Rock:
			return "Win", "Spock vaporizes Rock"
		elif Element == Spock:
			return "Tie", "Spock equals Spock"
		elif Element == Scissors:
			return "Win", "Spock smashes Scissors"
		elif Element == Lizard:
			return "Lose", "Lizard poisons Spock"
		else:
			raise NotImplementedError("Not yet implemented")
class Lizard(Element):
	def compareTo( Element):
		if Element == Paper:
			return "Win", "Lizard eats Paper"
		elif Element == Rock:
			return "Lose", "Rock crushes Lizard"
		elif Element == Spock:
			return "Win", "Lizard poisons Spock"
		elif Element == Scissors:
			return "Lose", "Scissors decapitates Lizard"
		elif Element == Lizard:
			return "Tie", "Lizard equals Lizard"
		else:
			raise NotImplementedError("Not yet implemented")


moves = [Rock, Paper, Scissors, Spock, Lizard]
