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


# def update_player_score():
#   if player_cards == [10, 11]:
#     print("blackjack")

#   if player_score > 21:
#     for card in player_cards:
#       if card == 11:
#         card = 1
#         player_score -= 10
#     return player_score

#   player_score = sum(player_cards)
#   return player_score

  


# game function
def game():

  
  print(logo)

  def deal_cards():
    player_turn = True
    computer_turn = False
    
    # player_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
    player_cards = [12, 12]
    player_score = sum(player_cards)
    print(player_cards, player_score)

    if player_cards == [10, 11]:
      print("black jack")

    if player_score > 21:
      print("over_21")
      for index, card in enumerate(player_cards):
        if not card == 11:
          print("game over")
        
        
        

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
        computer_turn = True
        print(player_score)

    def draw_computer_card():
      computer_cards.append(cards[random.choice(cards)])
      computer_score = sum(computer_cards)
      print(computer_cards, computer_score)

    while player_turn == False and computer_turn == True:
      computer_turn = False
      draw_computer_card()    

    if player_turn == False and computer_turn == False:
      print("game over")

  deal_cards()

# ask user if they want to start the game
if input(f"Do you want to play a game of blackjack? Type 'y' or 'n' ") == 'y':
  game()

  

