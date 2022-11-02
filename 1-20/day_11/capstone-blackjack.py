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


# game function
def game():
  
  print(logo)

  def deal_cards():  
    player_cards = [12, 11]
    # player_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
    player_score = sum(player_cards)
    # computer_cards = [cards[random.choice(cards)], cards[random.choice(cards)]]
    computer_cards = [3, 3]
    computer_score = sum(computer_cards)      

    # black jack conditions
    if player_cards.sort() == [10, 11]:
      return "player wins with a blackjack"
    
    if computer_cards.sort == [10, 11]:
      return "computer wins with a blackjack"
    
    # over_21 conditions
    if player_score > 21:
      if computer_score - 10 < 21:
        for i, card in enumerate(player_cards):
          if card == 11:
            player_cards[i] = 1
            player_score -= 10
            break
      else:
        print("bust")
    
    if computer_score > 21:
        for i, card in enumerate(player_cards):
          if card == 11:
            player_cards[i] = 1
            player_score -= 10
            break
        
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    computer_turn = False
    
    while input(f"Do you want to hit? Type 'y' or 'n' ") == 'y':
      player_cards.append(cards[random.choice(cards)])
      player_score = sum(player_cards)
      print(player_cards, player_score)
    else:
      print(player_cards, player_score)
      computer_turn = True

    while computer_turn == True and computer_score < 17:
      computer_cards.append(cards[random.choice(cards)])
      computer_score = sum(computer_cards)
      print(computer_cards, computer_score)

      if computer_score > 17:
        computer_turn = False

  deal_cards()

# ask user if they want to start the game
if input(f"Do you want to play a game of blackjack? Type 'y' or 'n' ") == 'y':
  game()

  

