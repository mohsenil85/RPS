class Element:
	def __init__(self, _name): #generic constructor
		self._name = _name

	def name(self):
		return self._name

	def compareTo(self, Element):
		raise NotImplementedError("Not yet implemented")

class Rock(Element):
	"Rock" #the doc string is returned so that interactivity is easier to metaprogram.  So that i could write things like print(element.e.__doc__, "has attatcked"),
	#and not have to define it for each element
	def compareTo(self, Element):
		if Element == Rock:#i'm sure there's cleaner way to implement this, but each case was so subtly different.  If i were to start this again, i'd have each elementj
			return "Tie", "Rock equals Rock"# use the builtin functions like __gt__ et al.
		elif Element == Paper:
			return "Lose", "Rock gets covered by Paper"
		elif Element == Spock:
			return "Lose", "Rock gets vaporized by Spock"
		elif Element == Scissors:
			return "Win", "Rock crushes Scissors"
		elif Element == Lizard:
			return "Win", "Rock crushes Lizard"
		else:
			raise NotImplementedError("Not yet implemented")
	

class Scissors(Element):
	"Scissors"
	def compareTo(self, Element):
		if Element == Scissors:
			return "Tie", "Scissors equals Scissors"
		elif Element == Paper:
			return "Win", "Scissors cuts Paper"
		elif Element == Spock:
			return "Lose", "Scissors get smashed by Spock"
		elif Element == Rock:
			return "Lose", "Scissors get crushed by Rock"
		elif Element == Lizard:
			return "Win", "Scissors decapitate Lizard"
		else:
			raise NotImplementedError("Not yet implemented")
		
class Paper(Element):
	"Paper"
	def compareTo(self, Element):
		if Element == Paper:
			return "Tie", "Paper equals Paper"
		elif Rock == Element:
			return "Win", "Paper covers Rock"
		elif Element == Rock:
			return "Win", "Paper covers Rock"
		elif Element == Spock:
			return "Win", "Paper disproves Spock"
		elif Element == Scissors:
			return "Lose", "Paper gets cut by Scissors"
		elif Element == Lizard:
			return "Lose", "Paper gets eaten by Lizard"
		else:
			raise NotImplementedError("Not yet implemented")

class Spock(Element):
	"Spock"
	def compareTo(self, Element):
		if Element == Paper:
			return "Lose", "Spock gets disproven by Paper"
		elif Element == Rock:
			return "Win", "Spock vaporizes Rock"
		elif Element == Spock:
			return "Tie", "Spock equals Spock"
		elif Element == Scissors:
			return "Win", "Spock smashes Scissors"
		elif Element == Lizard:
			return "Lose", "Spock gets poison by Lizard"
		else:
			raise NotImplementedError("Not yet implemented")
class Lizard(Element):
	"Lizard"
	def compareTo(self, Element):
		if Element == Paper:
			return "Win", "Lizard eats Paper"
		elif Element == Rock:
			return "Lose", "Lizard gets crushed by Rock"
		elif Element == Spock:
			return "Win", "Lizard poisons Spock"
		elif Element == Scissors:
			return "Lose", "Lizard gets decapitated by Scissors"
		elif Element == Lizard:
			return "Tie", "Lizard equals Lizard"
		else:
			raise NotImplementedError("Not yet implemented")


moves = [Rock, Paper, Scissors, Spock, Lizard]
