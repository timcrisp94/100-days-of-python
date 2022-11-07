from art import logo, vs
from game_data import data

# generate random numbers to select data
from random import randint
def get_data():
  return data[randint(0, len(data))]

# get_data()


# format data to compare followers
def format_data(person):
  name = person[name]
  description = person[description]
  country = person[country]
  return f"{name} a {description} from {country}"
  

# check answer function
guess = input("Who has more followers? A or B? ")

# TODO create compare function to compare A or B to player guess
# TODO create game_over function



# print(logo)
# print(vs)
# print(data[0])