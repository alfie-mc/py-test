import itertools, random

deck = list(itertools.product(range(1,14),['Spade(s)','Heart(s)','Diamond(s)','Club(s)']))

random.shuffle(deck)

print("Your cards are!")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
