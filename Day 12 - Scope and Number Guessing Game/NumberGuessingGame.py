#import variables
import random
from art import logo
print(logo)

print("Welcome to the guessing game! ")
print("I'm thinking of a number between 1 and 100.")


#global variables
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")
random_number_generator = random.randint(0,100)
print(random_number_generator)

#functions
# easy mode allows the user 10 guesses
def easy_mode():
    attempts = 9
    print("You have 10 attempts remaining to guess the number!")
    for guess in range(0,10):
        number = input("Make a Guess: ")
        print(f"You have {attempts} attempts remaining to guess the number!")

        if int(number) > random_number_generator:
            print("Too High.")
            attempts -= 1
        elif int(number) < random_number_generator:
            print("Too Low.")
            attempts -= 1
        elif int(number) == random_number_generator:
            print("You got it!")
            exit()
        else:
            print("Invalid choice")
    print("You ran out of guesses!")



# hard mode is the same as easy, but with 5 guess instead of 10
def hard_mode():
    attempts = 4
    print("You have 5 attempts remaining to guess the number!")
    for guess in range(0,5):
        number = input("Make a Guess: ")
        print(f"You have {attempts} attempts remaining to guess the number!")

        if int(number) > random_number_generator:
            print("Too High.")
            attempts -= 1
        elif int(number) < random_number_generator:
            print("Too Low.")
            attempts -= 1
        elif int(number) == random_number_generator:
            print("You got it!")
            exit()
        else:
            print("Invalid choice")
    print("You ran out of guesses!")



# Define which mode will be ran
if difficulty == 'easy':
    easy_mode()
elif difficulty == 'hard':
    hard_mode()
else:
    print("Invalid")
