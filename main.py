# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0




def start():
    """This function takes the input from the user and returns with the Dictionary"""
    global ask_user
    ask_user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ask_user == "espresso" or ask_user == "latte" or ask_user == "cappuccino" or ask_user == "off":
        if ask_user == "off":
            return 0
        else:

            return MENU[ask_user]
    elif ask_user == "report":
        report(money)
        return start()
    else:
        print("Wrong Entry!!")
        return start()


def report(money):
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {resources[key]}ml")
        else:
            print(f"{key.capitalize()}: {resources[key]}g")
    print(f"Money: {money}$")





# print(requirements)
def check():
    global want
    global requirements
    if start() != 0:

        want = start()
        requirements = want['ingredients']
        for component in requirements:
            if requirements[component] >= resources[component]:
                print(f"Sorry there is not enough {component}.")
                return start()
        return True
    else:
        return False


do_you_want = True


def money_check(money):
    while do_you_want:
        if check():
            cost = want['cost']
            print(f"Insert ${cost}")
            quarters = 0.25 * int(input("How many quarters?: "))
            dimes = 0.10 * int(input("How many dimes?: "))
            nickels = 0.05 * int(input("How many nickels?: "))
            pennies = 0.01 * int(input("How may pennies?: "))
            money = money + quarters + dimes + nickels + pennies
            # print(money)
            if money == cost:
                return True
            elif money > cost:
                print(f"Here is ${money - cost} dollars in change.")
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")
                return 0
        else:
            return False


def make_coffee():
    if money_check(money):
        for component in requirements:
            resources[component] -= requirements[component]
    else:
        return False


def machine():
    if make_coffee():
        print(f"Here is your 🍮{ask_user}")
        print(resources)
        return machine()


machine()
