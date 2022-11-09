"""
# 1. Print Report
# 2. Check Resources Sufficient
# 3. Process Coins
# 4. Check Transaction Successful
# 5. Make Drink
 """

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
cash_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    # return all drinks available
    drinks = menu.get_items()
    order = input(f"What would you like to drink? ({drinks}): ")

    if order == "off":
        is_on = False
    elif order == "report":
        coffee_machine.report()
        cash_machine.report()
    else:
        drink_ordered = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink_ordered) and cash_machine.make_payment(drink_ordered.cost):
            coffee_machine.make_coffee(drink_ordered)
