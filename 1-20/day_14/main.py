from art import logo, vs
from game_data import data

# generate random numbers to select data
from random import randint
person_one = data[randint(0, len(data))]
person_two = data[randint(0, len(data))]
# print(person_one, person_two)


# TODO create compare function to compare A and B
def compare(person_one, person_two):
  person_one_follower_count = person_one["follower_count"]
  person_two_follower_count = person_two["follower_count"]
  # print(person_one_follower_count, person_two_follower_count)
  if person_one_follower_count > person_two_follower_count:
    return "A"
  else:
    return "B"

# compare(person_one=person_one, person_two=person_two)
# TODO create player guess function
# TODO create compare function to compare A or B to player guess
# TODO create game_over function



# print(logo)
# print(vs)
# print(data[0])