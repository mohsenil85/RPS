import random
import element as e
import players as p

rock = e.Rock('rock')
paper = e.Paper('paper')

print("simple testing case:  rock vs paper")
print( paper.compareTo(e.Rock))
print()

s = p.StupidBot('dumb')

print("testing case of stupid bot vs each case")
print(s.play())
print(s.play().compareTo(rock))
print()
print(s.play(s.getPlayed()))
print(s.play(e.Scissors))
print(s.play(e.Paper))
print(s.play(e.Lizard))
print(s.play(e.Spock))
print()

r = p.RandomBot('rando')

print("test case of randombot vs rock twice")
print(r.play(e.Rock))
print(r.play(e.Rock))
print()

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
print("success")
