from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
menu_beverages = Menu()
machine = MoneyMachine()

IS_ON = True
one_drink = menu_beverages.menu[0].cost
print(one_drink)
drink_index = 0
cost = 0

while IS_ON:
    action = input("Would you like to choose a beverage? Type [y] for yes or [n] for no: ")
    if action == "y":
        drink = input(f"What beverage would you like? {menu_beverages.get_items()} ")
        item = menu_beverages.find_drink(drink)
        cost = menu_beverages.find_drink(drink).cost

        if maker.is_resource_sufficient(item):
            payment_ok = machine.make_payment(cost)

            if payment_ok:
                maker.make_coffee(item)

        else:
            print("You don't have enough resources.")
            maker.report()

    elif action == "report":
        maker.report()
        machine.report()
    elif action == "fill":
        maker.resources["water"] += int(input("How many mL of water do you want to add? "))
        maker.resources["milk"] += int(input("How many mL of milk do you want to add? "))
        maker.resources["coffee"] += int(input("How many g of coffee do you want to add? "))
        maker.report()
        machine.report()
    else:
        IS_ON = False

