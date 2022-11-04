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

print(f"You have {guesses} attempts remaining to guess the number")

while guesses > 0:
  guess = int(input("Make a guess: "))
  if not guess == number:
    guesses -= 1
    if guess < number:
      print("Too low")
    else:
      print("Too high")
    print(f"Guess again.\nYou have {guesses} attempts remaining to guess the number")
  else:
    guesses = 0
    print (f"You got it! The answer was {number}")