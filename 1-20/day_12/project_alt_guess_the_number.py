"""
initially completed the project by writing user stories and creating variables and conditions
looking at the finished repl, i decided to go back and build using functions
we're going to create functions to
-check user answer against actual answer
-set difficulty level to a global variable
-game()
"""

from art import logo
import random

# global difficulty variable 
EASY_LEVEL = 10
HARD_LEVEL = 5

# check user answer against actual answer
def check_answer(guess, answer, turns):
  # compare guess to answer
    # return number of turns remaining
  if guess > answer:
    print("Too hight")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer is {answer}")

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty[0] == 'e':
    return EASY_LEVEL
  else:
    return HARD_LEVEL

def game():
  
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  number = random.randint(1, 101)
  # test
  # print(f"the number is {number}")

  # set number of turns = set_difficulty()
  turns = set_difficulty()
  # guess until out of turns
  guess = 0
  while not guess == number:
    print(f"You have {turns} attempts remaining to guess the number")
    
    # let user guess a number
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, number, turns)
    if turns == 0:
      print("You're out of guesses, you lose")
      return
    elif guess != number:
      print("Guess again.")

game()