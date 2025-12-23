# Coffee Machine Simulator

A Python-based coffee machine simulator that models the operation of a real coffee vending machine. This project demonstrates object-oriented programming principles through a simple, interactive command-line application.

## Overview

This coffee machine simulator allows users to:
- Order different types of coffee drinks (espresso, latte, cappuccino)
- Insert coins to pay for drinks
- Check available resources and machine status
- Receive change when overpaying

The project is built using object-oriented design with separate classes handling different aspects of the coffee machine's functionality.

## Features

- **Menu Management**: Browse available drinks with pricing
- **Resource Tracking**: Monitor water, milk, and coffee levels
- **Payment Processing**: Accept coins and calculate change
- **Inventory Management**: Automatically deduct ingredients after each order
- **Status Reports**: View current resources and profit

## Available Drinks

| Drink | Water (ml) | Milk (ml) | Coffee (g) | Price |
|-------|------------|-----------|------------|-------|
| Espresso | 50 | 0 | 18 | $1.50 |
| Latte | 200 | 150 | 24 | $2.50 |
| Cappuccino | 250 | 50 | 24 | $3.00 |

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run the main program:
   ```bash
   python main.py
   ```

## Usage

When you run the program, you'll be prompted to:

1. **Choose a drink**: Type `espresso`, `latte`, or `cappuccino`
2. **Insert coins**: Enter the number of quarters, dimes, nickels, and pennies
3. **Receive your drink**: If payment is sufficient and resources are available

### Special Commands

- Type `report` to see current resource levels and profit
- Type `off` to shut down the machine

## Project Structure

```
coffee-machine/
├── main.py           # Main program loop and user interface
├── menu.py           # Menu and MenuItem classes
├── coffee_maker.py   # CoffeeMaker class for resource management
├── money_machine.py  # MoneyMachine class for payment processing
└── README.md         # This file
```

## Classes

- **MenuItem**: Represents individual drinks with ingredients and pricing
- **Menu**: Manages the collection of available drinks
- **CoffeeMaker**: Handles resource management and coffee preparation
- **MoneyMachine**: Processes payments and tracks profit

## Learning Objectives

This project demonstrates:
- Object-oriented programming (OOP) principles
- Class design and encapsulation
- Method implementation and interaction between classes
- User input validation and error handling
- Basic business logic simulation

## Requirements

- Python 3.x
- No external dependencies required

## Example Session

```
Which drink would you like? latte/espresso/cappuccino/? latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```
