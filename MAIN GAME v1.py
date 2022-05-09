import time
import random

def strip_string(string):
    return "".join(string.rstrip().lstrip())


def game_start(last_q, score):
    question = str(random.randint(1, 10))
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
    correct = {
        1: "Nice!",
        2: "Awesome!",
        3: "Great!",
        4: "Better than mama!"
    }
    incorrect = {
        1: "Nice try!",
        2: "Almost, but not quite!"
    }
    while question == last_q:
        question = str(random.randint(1, 10))
    answer = strip_string(input(f"What is {te_reo_numbers[question]}"))
    if answer == question:
        score += 1
        print(correct[random.randint(1, 4)])
        last_q = question
        time.sleep(0.4)
        game_start(last_q, score)
    else:
        print(f"{incorrect[random.randint(1, 2)]} You're score was: {score} points")


# Main
# Game start
x = 0
game_start(x, x)
