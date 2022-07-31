from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_on = True
while coffee_on:
    user_choice = input(f"  What would you like? {menu.get_items()}: ")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        coffee_on = False
    else:
        drink = menu.find_drink(user_choice)
        print(f"        Drink: {drink.name}, Amount: ${drink.cost}")    
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)