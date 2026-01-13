from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO-1 :  print report

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


money_machine.report()
coffee_maker.report()

# TODO-2 : check resources sufficient
# TODO-3 : process coins
# TODO-4 : Check transaction successful?
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        