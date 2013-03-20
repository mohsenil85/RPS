import random
import element as e
import players as p

rock = e.Rock('rock')
paper = e.Paper('paper')
scissors = e.Scissors('scissors')
spock = e.Spock('spock')
lizard = e.Lizard('lizard')

print("simple testing case:  rock vs paper")
print( paper.compareTo(e.Rock))
print( rock.compareTo(e.Paper))
print()

s = p.StupidBot('dumb')

print("testing case of stupid bot vs each case")
print(s.play(e.Rock))
print(s.play(e.Scissors))
print(s.play(e.Paper))
print(s.play(e.Lizard))
print(s.play(e.Spock))
print()

print("testing case of stupidbot vs stupid bot!")
s1 = p.StupidBot('stupid1')
s2 = p.StupidBot('stupid2')

print(s1.play(s2.getPlayed()))
print(s2.play(s1.getPlayed()))
print()


print("test case of randombot vs rock twice")
r = p.RandomBot('rando')
s2 = p.StupidBot('stupid2')
print(r.play(s2.getPlayed()))
print(r.play(s2.getPlayed()))
print()


print("test case of randombot vs randombot 5 times")
for i in range(5):
	r = p.RandomBot('rando')
	r1 = p.RandomBot('rando1')
	print(r.play(r1.getPlayed()))
print()

print("test case of randombot vs stupidbot")

stupid = p.StupidBot('stupid')
random = p.RandomBot('random')
for i in range(5):
	print(stupid.play(random.getPlayed()))
	print(random.play(stupid.getPlayed()))

print("test case of itrate ive booooot  vs all cases twice")
i = 0
itr = p.IterativeBot('itr', i)
print(itr.play(e.Rock))
print(itr.play(e.Scissors))
print(itr.play(e.Paper))
print(itr.play(e.Lizard))
print(itr.play(e.Spock))
print(itr.play(e.Rock))
print(itr.play(e.Scissors))
print(itr.play(e.Paper))
print(itr.play(e.Lizard))
print(itr.play(e.Spock))


print()
print("test case of last play bot")
lp = p.LastPlayBot('lpb', e.Rock)
print(lp.play(e.Scissors))
print(lp.play(e.Paper))
print(lp.play(e.Lizard))
print(lp.play(e.Spock))
print(lp.play(e.Rock))
print(lp.play(e.Scissors))


print()
print("test case of last play bot vs randombot 5 times")
for i in range(5):
	print(lp.play(random.getPlayed()))

print()
print("test case of last play bot vs itatebot 5 times")
for i in range(5):
	print(lp.play(itr.getPlayed()))
print()

print()
print("test case of  iterative bot vs last play bot 5 times")
for i in range(5):
	print(itr.play(lp.getPlayed()))

print("human testing")
h = p.Human('human')
h.play()

print("success")
