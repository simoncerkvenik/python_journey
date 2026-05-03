import random

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards)

print(cards)


cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
cards2 = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

random.seed(10)
random.shuffle(cards)

random.seed(10)
random.shuffle(cards2)

print(cards, cards2)