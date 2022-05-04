import random
import time


def strip_string(string):
    return "".join(string.rstrip().lstrip())


def game_start(score, last_q):
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
    if answer == question:
        score += 1
        print("Nice!")
        last_q = question
        time.sleep(0.4)
        game_start(score, last_q)
    else:
        print(f"Incorrect! You're score was: {score} points")


# Variables
score_keep = 0
question_keep = 2147483647

# Main
print("Welcome to the Te Reo Counting Quiz!\n"
      "*clapping sounds*\n"
      "Now time to introduce the contestant for tonight!")
time.sleep(0.4)
name = input("Whats your name?: ")
time.sleep(0.4)
print(f"Welcome, {name}, to the Show!\n")
time.sleep(0.8)
print("I hope you brushed up on your Te Reo skills, this will be a Time Trial Quiz!\n"
      "But first the rules of the game\n"
      "There will be a word that pops up on your screen\n"
      "Just type the number that corresponds to that number and just need to type it out and press enter!")
time.sleep(0.8)
print("Hope you're ready!")
time.sleep(1.4)
# Game start
game_start(score_keep, question_keep)
