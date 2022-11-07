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



# print(logo)
# print(vs)
# print(data[0])

game()