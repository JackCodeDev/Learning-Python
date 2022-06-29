from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_oder = Menu()


continue_order = True
while continue_order:
    options = menu_oder.get_items()
    choice = input(f"Would you like to drink? ({options}) ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        continue_order = False
    else:
        drink = menu_oder.find_drink(choice)
        coffee_maker.is_resource_sufficient(drink)
        payment = money_machine.process_coins()
        if payment >= drink.cost:
            coffee_maker.make_coffee(drink)









