import time
import sys

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

#defining the money
quarter = 0.25
dime = .10
penny = .1
nickel = .5
dollar = 1.0

shutdown = False

while not shutdown:
    #Ask the user what drink they would like to make
    user_choice = input("What would you like?\n- espresso \n- latte\n- cappuccino\n- Shutdown\n- Report\nChoice: ").lower()


    def brewing_coffee():
        print("Brewing your espresso...")
        stages = ["Heating water", "Grinding beans", "Extracting", "Finishing"]

        for stage in stages:
            print(f"{stage}...", end="")
            for i in range(3):
                print(".", end="")
                sys.stdout.flush()
                time.sleep(0.5)
            print(" ✓")

        print("☕ Your espresso is ready!")


    def brewing_latte():
        print("Brewing your latte...")
        stages = ["Heating water", "Grinding beans", "Extracting espresso", "Steaming milk", "Combining", "Finishing"]

        for stage in stages:
            print(f"{stage}...", end="")
            for i in range(3):
                print(".", end="")
                sys.stdout.flush()
                time.sleep(0.5)
            print(" ✓")

        print("☕ Your latte is ready!")


    def brewing_cappuccino():
        print("Brewing your cappuccino...")
        stages = ["Heating water", "Grinding beans", "Extracting espresso", "Steaming milk", "Creating thick foam",
                  "Layering", "Dusting with cocoa", "Finishing"]

        for stage in stages:
            print(f"{stage}...", end="")
            for i in range(3):
                print(".", end="")
                sys.stdout.flush()
                time.sleep(0.5)
            print(" ✓")

        print("☕ Your cappuccino is ready!")


    def expresso():
        expresso_data = MENU["espresso"]
        expresso_ingredients = expresso_data["ingredients"]
        water_requirement = expresso_ingredients["water"]
        coffee_requirement = expresso_ingredients["coffee"]
        cost = expresso_data["cost"]

        #Determine if there is enough coffee and water to make expresso
        if water_requirement > resources["water"]:
            print("Not Enough Water available!")
            exit()
        else:
            print("---Sufficient water available---")

        if coffee_requirement > resources["coffee"]:
            print("Not Enough Coffee available!")
            exit()
        else:
            print("---Sufficient coffee available---")

        #Determine if user has enough money to pay for the drink
        money_submitted = 0.0
        while money_submitted < cost:
            coin = input("Insert coin (quarter/dime/nickel/penny/dollar) or 'done': ").lower()
            if coin == "done":
                break
            elif coin == "quarter":
                money_submitted += quarter
                print(f"Added $0.25. Total: ${money_submitted:.2f}")
            elif coin == "dime":
                money_submitted += dime
                print(f"Added $0.10. Total: ${money_submitted:.2f}")
            elif coin == "nickel":
                money_submitted += nickel
                print(f"Added $0.05. Total: ${money_submitted:.2f}")
            elif coin == "penny":
                money_submitted += penny
                print(f"Added $0.01. Total: ${money_submitted:.2f}")
            elif coin == "dollar":
                money_submitted += dollar
                print(f"Added $1.00. Total: ${money_submitted:.2f}")
            else:
                print("Invalid coin. Please use: quarter, dime, nickel, or penny")

        if money_submitted == cost:
            print("Thank you, pouring drink now!\n")
            brewing_coffee()

        if money_submitted > cost:
            change = money_submitted - cost
            if change > 0:
                print(f"Here's your change: ${change:.2f}")
                print("Thank you, pouring drink now!\n")
                brewing_coffee()

            #Subtract the resources used from available resources
            resources["water"] -= water_requirement
            resources["coffee"] -= coffee_requirement
            print(resources["water"])
            print(resources["coffee"])
        else:
            print("Insufficient funds")




    def latte():
        latte_data = MENU["latte"]
        ingredients = latte_data["ingredients"]
        water_requirement = ingredients["water"]
        coffee_requirement = ingredients["coffee"]
        milk_requirement = ingredients["milk"]
        cost = latte_data["cost"]

        #determine if there is enough coffee, water, and milk for a latte
        if water_requirement > resources["water"]:
            print("Not Enough Water available!")
            exit()
        else:
            print("---Sufficient water available---")

        if coffee_requirement > resources["coffee"]:
            print("Not Enough Coffee available!")
            exit()
        else:
            print("---Sufficient coffee available---")


        if milk_requirement > resources["milk"]:
            print("Not Enough Milk Available")
            exit()
        else:
            print("---Sufficient Milk available---")

        #Determine if user has enough money to pay for the drink
        money_submitted = 0.0
        while money_submitted < cost:
            coin = input("Insert coin (quarter/dime/nickel/penny/dollar) or 'done': ").lower()
            if coin == "done":
                break
            elif coin == "quarter":
                money_submitted += quarter
                print(f"Added $0.25. Total: ${money_submitted:.2f}")
            elif coin == "dime":
                money_submitted += dime
                print(f"Added $0.10. Total: ${money_submitted:.2f}")
            elif coin == "nickel":
                money_submitted += nickel
                print(f"Added $0.05. Total: ${money_submitted:.2f}")
            elif coin == "penny":
                money_submitted += penny
                print(f"Added $0.01. Total: ${money_submitted:.2f}")
            elif coin == "dollar":
                money_submitted += dollar
                print(f"Added $1.00. Total: ${money_submitted:.2f}")
            else:
                print("Invalid coin. Please use: quarter, dime, nickel, or penny")

        if money_submitted == cost:
            print("Thank you, pouring drink now!\n")
            brewing_latte()

        if money_submitted > cost:
            change = money_submitted - cost
            if change > 0:
                print(f"Here's your change: ${change:.2f}")
                print("Thank you, pouring drink now!\n")
                brewing_latte()

            #Subtract the resources used from available resources
            resources["water"] -= water_requirement
            resources["coffee"] -= coffee_requirement
            resources["milk"] -= milk_requirement


    def cappuccino():
        cappuccino_data = MENU["cappuccino"]
        ingredients = cappuccino_data["ingredients"]
        water_requirement = ingredients["water"]
        coffee_requirement = ingredients["coffee"]
        milk_requirement = ingredients["milk"]
        cost = cappuccino_data["cost"]

        #determine if there is enough coffee, water, and milk for a latte
        if water_requirement > resources["water"]:
            print("Not Enough Water available!")
            exit()
        else:
            print("---Sufficient water available---")

        if coffee_requirement > resources["coffee"]:
            print("Not Enough Coffee available!")
            exit()
        else:
            print("---Sufficient coffee available---")


        if milk_requirement > resources["milk"]:
            print("Not Enough Milk Available")
            exit()
        else:
            print("---Sufficient Milk available---")

        #Determine if user has enough money to pay for the drink
        money_submitted = 0.0
        while money_submitted < cost:
            coin = input("Insert coin (quarter/dime/nickel/penny/dollar) or 'done': ").lower()
            if coin == "done":
                break
            elif coin == "quarter":
                money_submitted += quarter
                print(f"Added $0.25. Total: ${money_submitted:.2f}")
            elif coin == "dime":
                money_submitted += dime
                print(f"Added $0.10. Total: ${money_submitted:.2f}")
            elif coin == "nickel":
                money_submitted += nickel
                print(f"Added $0.05. Total: ${money_submitted:.2f}")
            elif coin == "penny":
                money_submitted += penny
                print(f"Added $0.01. Total: ${money_submitted:.2f}")
            elif coin == "dollar":
                money_submitted += dollar
                print(f"Added $1.00. Total: ${money_submitted:.2f}")
            else:
                print("Invalid coin. Please use: quarter, dime, nickel, or penny")

        if money_submitted == cost:
            print("Thank you, pouring drink now!\n")
            brewing_cappuccino()

        if money_submitted > cost:
            change = money_submitted - cost
            if change > 0:
                print(f"Here's your change: ${change:.2f}")
                print("Thank you, pouring drink now!\n")
                brewing_cappuccino()

            #Subtract the resources used from available resources
        resources["water"] -= water_requirement
        resources["coffee"] -= coffee_requirement
        resources["milk"] -= milk_requirement




    def shutdown_animation():
        print("Coffee machine will shut down in:")

        for i in range(3, 0, -1):
            print(f"  {i}...", flush=True)
            time.sleep(1)

        print("  Shutting down now!")
        time.sleep(0.5)

        # Power down animation
        power_levels = ["████████", "██████░░", "████░░░░", "██░░░░░░", "░░░░░░░░"]
        for level in power_levels:
            print(f"\rPower: [{level}]", end="", flush=True)
            time.sleep(0.3)

        print("\n☕ Coffee machine is now off. Goodbye!")

    if user_choice == "espresso":
        expresso()
    elif user_choice == "latte":
        latte()
    elif user_choice == "cappuccino":
        cappuccino()
    elif user_choice == "shutdown":
        shutdown_animation()
        shutdown = True
    elif user_choice == "report":
        print(resources)
    else:
        print("invalid option")
