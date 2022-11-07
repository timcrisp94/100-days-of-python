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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# check resources to see if we have enough to make drink
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, we do not have enough {item}")
            return False
    return True

# function for processing coins
def process_coins():
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * .25
    total += int(input("how many dimes?: ")) * .10
    total = int(input("how many nickels?: ")) * .05
    total = int(input("how many pennies?: ")) * .01

is_on = True

while is_on:
    # prompt user by asking "what would you like?"
    selection = input("What would you like? espresso/latte/cappuccino): ")
    if selection == "off":
        is_on = False
    elif selection == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")