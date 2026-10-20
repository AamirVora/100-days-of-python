from importlib import resources

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

new_order = True

while new_order:
    get_items = menu.get_items()
    order_drink = input(f"What would you like to order? latte/cappuccino/espresso: ").lower()
    if order_drink == "report":
        coffee_report = coffeMaker.report()
        money_report = moneyMachine.report()
    elif order_drink == "off":
        new_order = False
    else:
        find_drink = menu.find_drink(order_drink)
        if coffeMaker.is_resource_sufficient(find_drink):
            if moneyMachine.make_payment(find_drink.cost):
                coffeMaker.make_coffee(find_drink)


