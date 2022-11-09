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
drink_menu = Menu()

is_on = True

while is_on:
    options = drink_menu.get_items()
    order = input("What would you like to drink? espresso/cappuccino/latte")