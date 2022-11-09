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

#
coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()
drink_menu = Menu()

spro = drink_menu.find_drink("espresso")
cap = drink_menu.find_drink("cappuccino")
tay = drink_menu.find_drink("latte")


def take_order(drink_order):
    if drink_order == "print report":
        coffee_machine.report()
    elif drink_order == "off":
        print("Goodbye")
    else:
        if coffee_machine.is_resource_sufficient(drink_order):
            return True
        else:
            return False


order = input("What would you like to drink? latte/espresso/cappuccino?: ")

take_order(order)