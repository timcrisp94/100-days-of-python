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

# compare function
def compare(player_score, computer_score):
  if player_score == computer_score:
    return "it's a draw"
  elif player_score == 0:
    return "Player wins with a blackjack!"
  elif computer_score == 0:
    return "Computer wins with a blackjack!"
  elif player_score > 21:
    return "Busted! You lose!"
  elif computer_score > 21:
    return "Computer busts! Player wins!"
  elif player_score > computer_score:
    return "Player wins!"
  else:
    return "Computer wins!"

# game function
def game():
  
  print(logo)
  game_over = False
  player_cards = []
  computer_cards = []

  for _ in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())
  

  while not game_over:
    player_score = update_score(player_cards)
    computer_score = update_score(computer_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if player_score == 0 or computer_score == 0 or player_score > 21:
      game_over = True
    else:
      if input(f"Do you want to hit? Type 'y' or 'n' ") == 'y':
        player_cards.append(deal_card())
      else:
        game_over = True

    while game_over == True and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = update_score(computer_cards)

    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

# ask user if they want to start the game
while input(f"Do you want to play a game of blackjack? Type 'y' or 'n' ") == 'y':
  clear()
  game()


