from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""
# 1. Print Report
# 2. Check Resources Sufficient
# 3. Process Coins
# 4. Check Transaction Successful
# 5. Make Drink
 """

#imported functions
coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    order = input("What would you like to drink? espresso/cappuccino/latte?: ")
    if order == "print report":
        coffee_machine.report()
        cash_register.report()
    elif order == "off":
        is_on = False
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) and cash_register.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)