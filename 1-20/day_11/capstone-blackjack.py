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

# deal card function
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# update score function
def update_score(cards):
  # check for blackjack hand
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # if over 21, check for an ace
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)



# game function
def game():
    

  print(logo)

  # def deal_cards():      
  #   player_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
  #   player_score = update_score(0, player_cards)
    
  #   computer_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
  #   computer_score = update_score(0, computer_cards)
    
  #   if over_21(player_score, player_cards):
  #     print("bust")
  #   elif over_21(computer_score, computer_cards):
  #     print("bust")
  #   else:
  #     print(f"Your cards: {player_cards}, current score: {player_score}")
  #     print(f"Computer's first card: {computer_cards[0]}")
    
  #   computer_turn = False
    
  #   while input(f"Do you want to hit? Type 'y' or 'n' ") == 'y':
  #     player_cards.append(cards[random.choice(cards)])
  #     player_score = update_score(player_score, player_cards)
  #     if not over_21(player_score, player_cards):
  #       print(player_score, player_cards)
  #   else:
  #     print(player_cards, player_score)
  #     computer_turn = True

  #   while computer_turn == True and computer_score < 17:
  #     computer_cards.append(cards[random.choice(cards)])
  #     update_score(computer_score, computer_cards)
  #     print(computer_cards, computer_score)

  #     if computer_score > 17:
  #       computer_turn = False

  # deal_cards()

# ask user if they want to start the game
if input(f"Do you want to play a game of blackjack? Type 'y' or 'n' ") == 'y':
  game()

  

