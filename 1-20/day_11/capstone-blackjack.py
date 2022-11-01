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
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

# environment variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_score = 0
computer_score = 0

# game function
def game():
  print(logo)
  def deal_cards():
    player_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
    player_score = sum(player_cards)

    computer_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
  deal_cards()

  def blackjack(score):
    if score == 21:
      return True
    else:
      return False

  def over_21(score, cards):
    if score > 21:
      for card in cards:
        if card == 11:
          card = 1
          score -= 10
    return score

  # test over_21
  # print(over_21(26, [11, 10, 5]))

# ask user if they want to start the game
if input(f"Do you want to play a game of blackjack? Type 'y' or 'n' ") == 'y':
  game()

  

