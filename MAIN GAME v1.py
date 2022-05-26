"""
This is the basic game.
It takes a random number and sends it through the dictionary and from there it prints.
Then it asks the player what number it is.
"""
import time
import random


def strip_string(string):
    return "".join(string.rstrip().lstrip())


def game_start(score):
    te_reo_numbers = {
        "1": "tahi",
        "2": "rua",
        "3": "toru",
        "4": "whā",
        "5": "rima",
        "6": "ono",
        "7": "whitu",
        "8": "waru",
        "9": "iwa",
        "10": "tekau"
    }
    question = str(random.randint(1, 10))
    answer = strip_string(input(f"What is {te_reo_numbers[question]}"))
    if answer == question:  # correct
        score += 1
        print("Correct!")
        time.sleep(0.4)
        game_start(score)
    else:  # incorrect
        print(f"Wrong! You're score was: {score} points")
        # no need for int checker, it will be wrong either way.
        # from here send to score board.


# Main
# Game start
game_start(0)
















