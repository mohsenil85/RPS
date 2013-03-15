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
print(s.play(e.Rock))
print(s.play(e.Scissors))
print(s.play(e.Paper))
print(s.play(e.Lizard))
print(s.play(e.Spock))
print()

r = p.RandomBot('rando')

print(r.play(e.Rock))
print(r.play(e.Rock))
