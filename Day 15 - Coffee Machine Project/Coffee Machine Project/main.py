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

refill_coffee = {
    "water": 50,
    "milk": 50,
    "coffee": 50,
}


new_order = True


def calculate_total_paid(user_input):
    quarters_value = 0.25
    dimes_value = 0.10
    nickels_value = 0.05
    pennies_value = 0.01
    cost_of_the_drink = MENU[user_input]["cost"]
    print(f"{user_input} is ${cost_of_the_drink}")
    print("Please insert coins.")
    how_many_quarters = float(input("How many quarters?: "))
    how_many_dimes = float(input("How many dimes?: "))
    how_many_nickels = float(input("How many nickles?: "))
    how_many_pennies = float(input("How many pennies?: "))
    total_quarters = how_many_quarters * quarters_value
    total_dimes = how_many_dimes * dimes_value
    total_nickels = how_many_nickels * nickels_value
    total_pennies = how_many_pennies * pennies_value
    total_price = round(total_quarters + total_dimes + total_nickels + total_pennies, 2)
    print(f"Paid total: ${total_price}")
    if cost_of_the_drink > total_price:
        print("Not enough money")
    else:
        change = round(total_price - cost_of_the_drink,2)
        print(f"Here's the change: ${change}")
        print(f"Here's your {user_input}. Have a great day!")
    return total_price

def check_ingredients_needed(user_input):

    if user_input == "cappuccino" or "latte" or "espresso":
        if user_input == "cappuccino" or user_input == "latte":
            milk_needed = MENU[user_input]["ingredients"]["milk"]
        water_needed = MENU[user_input]["ingredients"]["water"]
        coffee_needed = MENU[user_input]["ingredients"]["coffee"]

        if user_input == "latte" or user_input == "cappuccino":
            if resources["water"] < water_needed or resources["milk"] < milk_needed or resources["coffee"] < coffee_needed:
                print(f"Insufficient resources to make a {user_input}.")
            else:
                calculate_total_paid(user_input)
                resources["milk"] -= milk_needed
                resources["water"] -= water_needed
                resources["coffee"] -= coffee_needed
        elif user_input == "espresso":
            if resources["water"] < water_needed or resources["coffee"] < coffee_needed:
                print(f"Insufficient resources to make a {user_input}.")
            else:
                resources["water"] -= water_needed
                resources["coffee"] -= coffee_needed
                calculate_total_paid(user_input)
    else:
        print("Sorry that's not an option")


def check_price(user_input):
    cost_of_the_drink = MENU[user_input]["cost"]
    return cost_of_the_drink


while new_order:

    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        check_ingredients_needed(user_input)
    elif user_input == "report":
        print(f"Water : {water_left} ml \nMilk: {milk_left} ml \nCoffee: {coffee_left} gm")
    elif user_input == "refill":
        resources["water"] += refill_coffee["water"]
        resources["milk"] += refill_coffee["milk"]
        resources["coffee"] += refill_coffee["coffee"]
        print("Coffee machine refilled!")
    elif user_input == "off":
        new_order = False
        print("Machine shutting down!")
    else:
        print("Sorry, that's not a valid option")







