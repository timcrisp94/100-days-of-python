############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

from art import logo
from os import system, name
import random

# clear function
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# game function
def game():
  print(logo)
  def deal_cards():
    player = [cards[random.choice(cards)], cards[random.choice(cards)]]
    computer = [cards[random.choice(cards)], cards[random.choice(cards)]]
    print(player, computer)

  deal_cards()

if input(f"Do you want to play a game of blackjack? Type 'y' or 'no' ") == 'y':
  game()

  

