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


shutdown = False
while not shutdown:
    #Ask the user what drink they would like to make
    user_choice = input("What would you like?\n- espresso \n- latte\n- cappuccino\n- Shutdown\n Choice: ").lower()


    #printing the report of available resources
    print(f"Here are the available resources in Ml\n{resources}")


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
        money_submitted = float(input("Please enter coins to purchase drink "))
        if money_submitted == cost:
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
        money_submitted = float(input("Please enter coins to purchase drink: "))
        if money_submitted == cost:
            print("Thank you, pouring drink now!\n")
            brewing_latte()

            #Subtract the resources used from available resources
            resources["water"] -= water_requirement
            resources["coffee"] -= coffee_requirement
            resources["milk"] -= milk_requirement
            print(resources["water"])
            print(resources["coffee"])
            print(resources["milk"])
        else:
            print("Insufficient funds")


    #def cappuccino():


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
    #elif user_choice == "cappuccino":
     #   cappuccino()
    elif user_choice == "shutdown":
        shutdown_animation()
        shutdown = True



