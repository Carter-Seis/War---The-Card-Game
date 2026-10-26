#generate and shuffle a card deck
import random

# define all the things in the deck with suits.
deck = [Ace ♢, Two ♢, Three ♢, Four ♢, Five ♢, Six ♢, Seven ♢, Eight ♢, Nine ♢, Ten ♢, Jack ♢, Queen ♢, King ♢, Ace ♠, Two ♠, Three ♠, Four ♠, Five ♠, Six ♠, Seven ♠, Eight ♠, Nine ♠, Ten ♠, Jack ♠, Queen ♠, 
King ♠, Ace ♡, Two ♡, Three ♡, Four ♡, Five ♡, Six ♡, Seven ♡, Eight ♡, Nine ♡, Ten ♡, Jack ♡, Queen ♡, King ♡, Ace ♣, Two ♣, Three ♣, Four ♣, Five ♣, Six ♣, Seven ♣, Eight ♣, Nine ♣, Ten ♣

# Shuffle deck
random.shuffle(deck)
if deck != ""
print("Shuffled Deck: ")
for card in deck:
  print(card)

