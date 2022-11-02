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
player_cards = []
computer_cards = []

player_score = 0
computer_score = 0



# game function
def game():

  print(logo)

  def deal_cards():
    player_turn = True
    
    player_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
    player_score = sum(player_cards)

    computer_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
    
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    def draw_player_card():
      player_cards.append(cards[random.choice(cards)])
      player_score = sum(player_cards)
      print(player_cards, player_score)
    
    while player_turn == True:
      if input(f"Do you want to hit? Type 'y' or 'n' ") == 'y':
        draw_player_card()
      else:
        player_turn = False
        print(player_score)

    def draw_computer_card():
      computer_cards.append(cards[random.choice(cards)])
      computer_score = sum(computer_cards)
      print(computer_cards, computer_score)

    if player_turn == False:
      draw_computer_card()
      return 

  deal_cards()
  
  

  # # function to check if either player has blackjack
  # def blackjack(score):
  #   if score == 21:
  #     return True
  #   else:
  #     return False

  # # function to switch ace if over 21
  # def over_21(score, hand):
  #   if score > 21:
  #     for card in hand:
  #       if card == 11:
  #         card = 1
  #         score -= 10
  #   return score

  # test over_21
  # print(over_21(26, [11, 10, 5]))

  # test hit

  # while not blackjack(player_score) and not blackjack(computer_score):
  #   if not over_21(player_score, player_cards):
  #       print(hit(player_score, player_cards))
        # print(f"Your cards: {player_cards}, current score: {player_score}")






# ask user if they want to start the game
if input(f"Do you want to play a game of blackjack? Type 'y' or 'n' ") == 'y':
  game()

  

