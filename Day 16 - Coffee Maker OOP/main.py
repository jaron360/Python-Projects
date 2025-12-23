from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    items = menu.get_items()
    drink_choice = input(f"Which drink would you like? {items}?")
    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
