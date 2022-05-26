"""
I have rewritten all the code.
It seems more efficient.
"""
import time
import random


def strip_string(string):
    return "".join(string.rstrip().lstrip())


def main_game(name, score, previous):
    # variables
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
        4: "uh-huh!",
        1: "Yes!",
        2: "yeap.",
        3: "Safe."
    }
    incorrect = {
        5: "not really...",
        1: "Yew havin' a laugh?",
        2: "No way.",
        3: "Nuh-uh.",
        4: "yeah, nah"
    }
    number = str(random.randint(1, 10))
    # repeat remover and number/question generator
    while number == previous:
        number = str(random.randint(1, 10))
    question = te_reo_numbers[number]  # expected example: "waru"
    answer = strip_string(input(f"What is {question}?"))  # expected example: "8"
    if number == answer:  # correct
        time.sleep(0.1)
        print(f"{correct[random.randint(1, len(correct))]}")
        previous = number
        score += 1
        time.sleep(0.5)
        main_game(name, score, previous)
    else:  # incorrect
        time.sleep(0.3)
        print(f"{incorrect[random.randint(1, len(incorrect))]} You're score was: {score} points")


main_game(input("What is your name? : "), 0, 0)



















