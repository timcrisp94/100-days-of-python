MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO print report
# TODO check resources
# TODO process coins
# TODO check if enough money
# TODO make drink

# scripts

# "Please insert coins."
# 
# "How many dimes?: "
# "How many nickels?: "
# "How many nickels?: "
# "Here is ${change} in change."
# "Here is your {drink}. Enjoy"

# ask user what drink they would like
choice = input("What would you like? (espresso, latte, cappuccino): ")

# ask user to insert coins
def accept_coins():
  total = int(input("How many quarters?: ")) * .25
  total += int(input("How many dimes?: ")) * .10
  total += int(input("How many nickels?: ")) * .05
  total += int(input("How many pennies?: ")) * .01
  return total

  print(total)

accept_coins()