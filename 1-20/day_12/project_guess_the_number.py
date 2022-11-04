from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 101)
print(f"the number is {number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty[0] == 'e':
  guesses = 10
else:
  guesses = 5



# number = random.randint(1, 101)

input("Make a guess: ")
# if 