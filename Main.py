# main.py
import matplotlib.pyplot as plt
from shuffle_deck import create_and_save_deck

# Step 1: Create and save the shuffled deck using File I/O
create_and_save_deck()

print("\nLet's Play War!")

# Step 2: Read the deck back from deck.txt using basic File I/O
deck1 = []
deck2 = []

file = open("deck.txt", "r")
lines = file.readlines()
file.close()

# Split lines into deck 1 and deck 2 using a simple loop
index = 0
for line in lines:
    line = line.strip()
    parts = line.split(",")
    card_name = parts[0]
    card_val = int(parts[1])
    
    card = [card_name, card_val]
    
    if index < 26:
        deck1.append(card)
    else:
        deck2.append(card)
        
    index = index + 1

choice = input("Choose a deck 1 or 2: ")

if choice == "1":
    your_deck = deck1
    opponent_deck = deck2
else:
    your_deck = deck2
    opponent_deck = deck1

round_num = 1
wins = 0
losses = 0
ties = 0

# Game Loop
while len(your_deck) > 0 and len(opponent_deck) > 0:
    print("\nLet's Play round " + str(round_num))
    
    # Draw top card (first item in the list)
    your_card = your_deck[0]
    opponent_card = opponent_deck[0]
    
    # Remove top cards from decks
    your_deck.remove(your_card)
    opponent_deck.remove(opponent_card)
    
    print("Your Card: " + your_card[0] + "    Opponent Card: " + opponent_card[0])
    
    if your_card[1] > opponent_card[1]:
        print("You WIN Round " + str(round_num))
        your_deck.append(your_card)
        your_deck.append(opponent_card)
        wins = wins + 1
    elif your_card[1] < opponent_card[1]:
        print("You LOSE Round " + str(round_num))
        opponent_deck.append(your_card)
        opponent_deck.append(opponent_card)
        losses = losses + 1
    else:
        print("You TIE Round " + str(round_num))
        your_deck.append(your_card)
        opponent_deck.append(opponent_card)
        ties = ties + 1
        
    print("you have " + str(len(your_deck)) + " cards opponent has " + str(len(opponent_deck)) + " cards")
    
    user_choice = input("Would you like to play the next round?\nY/no i'd like to stop playing\n")
    if user_choice.lower() == "no" or user_choice.lower() == "n":
        break
        
    round_num = round_num + 1

# Game Statistics
print("\nGame Stats:")
print("Wins: " + str(wins))
print("Losses: " + str(losses))
print("Ties: " + str(ties))
print("Your final card count: " + str(len(your_deck)))
print("Opponent final card count: " + str(len(opponent_deck)))

# Simple Bar Chart for Wins, Losses, and Ties (No subplots!)
outcomes = ["Wins", "Losses", "Ties"]
counts = [wins, losses, ties]

plt.figure()
plt.bar(outcomes, counts)
plt.title("Round Outcomes (Wins, Losses, Ties)")
plt.xlabel("Outcome")
plt.ylabel("Total Count")
plt.show()