from menu import Menu
from resources import ingredients
from change import changeMachine
change = changeMachine()
resources = ingredients()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"Select a beverage? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        resources.report()
        change.report()
    else:
        drink = menu.find_drink(choice)
        if resources.is_resource_sufficient(drink) and change.make_payment(drink.cost):
          resources.make_coffee(drink)
