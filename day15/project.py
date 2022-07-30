#COFFEE MACHINE
import math
from coffee_ingredients import MENU, resources

money = 0


def report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Money: ${round(money, 2)}")


def check_fund(user_selection, total_amount):
    coffee_selected = {}
    for coffee in MENU:
        if user_selection == coffee:
            coffee_selected[coffee] = MENU[coffee]

    if total_amount >= coffee_selected[user_selection]['cost']:
        if total_amount - coffee_selected[user_selection]['cost'] > 0:
            return total_amount - coffee_selected[user_selection]['cost']
        else:
            return 'no change'
    else:
        return False


def check_ingredients(user_selection):
    coffee_selected = {}
    for coffee in MENU:
        if user_selection == coffee:
            coffee_selected[coffee] = MENU[coffee]
    if resources['water'] < coffee_selected[user_selection]['ingredients']['water']:
        return "Sorry there is not enough water"
    elif user_selection != 'espresso' and resources['milk'] < coffee_selected[user_selection]['ingredients']['milk']:
        return "Sorry there is not enough milk"
    elif resources['coffee'] < coffee_selected[user_selection]['ingredients']['coffee']:
        return "Sorry there is not enough coffee"
    else:
        return 1


def take_funds():
    print("Please insert coins.")
    quarters = float(input('how many quarters?: '))
    dimes = float(input('how many dimes?: '))
    nickles = float(input('how many nickles: '))
    pennies = float(input('how many pennies?: '))
    return (0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies)


def make_coffee(selected_coffee):
    water = MENU[selected_coffee]['ingredients']['water']
    milk = 0
    if selected_coffee != 'espresso':
        milk = MENU[selected_coffee]['ingredients']['milk']
    coffee = MENU[selected_coffee]['ingredients']['coffee']

    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    return MENU[selected_coffee]['cost']

def add():
    ingredient = input("What would you like to add?: ")
    amount = int(input("How much would you like to add? "))
    resources[ingredient] += amount
    print(f"      {amount}ml of {ingredient} successfully added ")
coffee_on = True
while coffee_on:
    user_choice = input("   What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        report()
    elif user_choice == "off":
        coffee_on = False
    elif user_choice == "add":
        add()
    else:
        funds = take_funds()
        checked_funds = check_fund(user_choice, funds)
        if checked_funds == False:
            print("Sorry that's not enough money. Money refunded.")
        else:
            checked_ingredients = check_ingredients(user_choice)
            if checked_ingredients == 1:
                price = make_coffee(user_choice)
                money += price
                if checked_funds != 'no change':
                    print(f"Here is ${round(checked_funds, 2)} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
            else:
                print(checked_ingredients)


