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

# global profit variable
profit = 0

# print resources function
def print_resources():
  for item in resources:
    name = item.upper()
    if item == "coffee":
      print(print(f"{name}: {resources[item]} g"))
    else:
      print(f"{name}: {resources[item]} ml")


# TODO check resources
"""
# check resources to confirm drink can be made
"""
def check_resources(drink_ingredients):  
  for key in drink_ingredients:
    if drink_ingredients[key] > resources[key]:
        print(f"I'm sorry there is not enough {key}")
        return False
  return True

# TODO process coins
# ask user to insert coins
def accept_coins():
  total = int(input("How many quarters?: ")) * .25
  total += int(input("How many dimes?: ")) * .10
  total += int(input("How many nickels?: ")) * .05
  total += int(input("How many pennies?: ")) * .01
  return total


# TODO check if enough money
# compare total from accept_coins to cost of drink
def complete_transaction(total_paid, total_cost):
  if total_paid >= total_cost:
    change = round(total_paid - total_cost, 2)
    print(f"Here is ${change} in change.")
    global profit 
    profit += total_cost
    return True
  else:
    print("I'm sorry, that's not enough")
    return False


# TODO make drink
def make_drink(drink_name, drink_ingredients):
  for item in drink_ingredients:
    resources[item] -= drink_ingredients[item]
  print(f"Here is your {drink_name}. Enjoy!")



is_on = True
while is_on:
  # ask user what drink they would like
  choice = input("What would you like? (espresso, latte, cappuccino): ")
  # TODO print report
  if choice == "off":
    is_on = False
  elif choice == "print report":
    print_resources()
  else:
    drink = MENU[choice]
    if check_resources(drink["ingredients"]):
      # initiate payment
      payment = accept_coins()
      # confirm payment
      if complete_transaction(payment, drink["cost"]):
        make_drink(choice, drink["ingredients"])

