import game_data
import art
import random

# art
print(art.logo)

score = 0

answer = True
while answer:
    # First comparison
    random_value_1 = random.choice(game_data.data)
    name = random_value_1['name']
    description = random_value_1['description']
    country = random_value_1['country']
    followers = random_value_1['follower_count']

    # Second Comparison
    random_value_2 = random.choice(game_data.data)
    name_2 = random_value_2['name']
    description_2 = random_value_2['description']
    country_2 = random_value_2['country']
    followers_2 = random_value_2['follower_count']


    # defining the print statement
    print(f"Compare A: {name}, a {description}, from {country}")
    print(art.vs)
    print(f"Against B: {name_2}, a {description_2}, from {country_2}")

    # take in the user guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # identify which has the most followers
    if followers > followers_2:
        correct_answer = 'A'
    else:
        correct_answer = 'B'

    # check if user is correct
    if guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}")

    else:
        print(f"Sorry, that's wrong. {name if correct_answer == 'A' else name_2} has more followers.")
        answer = False  # End the game
