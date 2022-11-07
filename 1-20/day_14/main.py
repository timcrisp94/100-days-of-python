from art import logo, vs
from game_data import data
import random
import os

# clear function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# generate random numbers to select data
def get_data():
  return random.choice(data)

# format data to compare followers
def format_data(person):
  name = person["name"]
  description = person["description"]
  country = person["country"]
  return f"{name} a {description} from {country}"
  
# check answer function
def check_answer(guess, person_a_followers, person_b_followers):
  if person_a_followers > person_b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  cls
  print(logo)
  score = 0
  game_over = False

  # generate persons a and b
  person_a = get_data()
  person_b = get_data()
  
  while not game_over:
    person_a = person_b
    person_b = get_data()

    while person_a == person_b:
      person_b = get_data()

      print(f"Compare A: {format_data(person_a)}")
      print(vs)
      print(f"Compare B: {format_data(person_b)}")

      guess = input("Who has more followers? Type 'A' or 'B': ").lower()
      a_follower_count = person_a["follower_count"]
      b_follower_count = person_b["follower_count"]

      is_correct = check_answer(guess, a_follower_count, b_follower_count)

      cls()
      print(logo)

      if is_correct:
        score += 1
        print(f"Correct! Current score: {score}")
      else:
        game_over = True
        print(f"Sorry that's wrong. Final score: {score}")
  
  
  play_again = input("Want to play again? Type 'Y' or 'N': ").lower()
  if play_again == "y":
    game()
    cls()
  

game()