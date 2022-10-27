# 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Start the game by asking the player:

# *"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

# From there you will need to figure out: 
# * How you will store the user's input.
# * How you will generate a random choice for the computer.
# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
# * And also how you will give feedback to the player. 
#Write your code below this line 👇

import random

print("Welcome to Rock, Paper, Scissors")
player_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, 2 for Scissors "))
computer_choice = random.randint(0, 2)


if player_choice == 0:
  print(rock)
elif player_choice == 1:
  print(paper)
else:
  print(scissors)

if computer_choice == 0:
  print(f"Computer chose:\n{rock}")
elif computer_choice == 1:
  print(f"Computer chose:\n{paper}")
else:
  print(f"Computer chose:\n{scissors}")


if player_choice == computer_choice:
  print("It's a tie, how exciting!")
else:
  if player_choice == 0:
    if computer_choice == 1:
      print("Paper covers Rock! Computer wins!")
    else:
      print("Rock beats Scissors! Player wins!")
  if player_choice == 1:
    if computer_choice == 0:
      print("Paper covers Rock! Player wins!")
    else:
      print("Rock beats Scissors! Computer wins!")

  if player_choice == 2:
    if computer_choice == 1:
      print(print("Rock beats Scissors! Computer wins!"))
    else: 
      print("Scissors beat paper! Player wins")


