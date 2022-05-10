import random
import time
import datetime


def yes_no(question_text):
    while True:
        # ask if they have played before
        answer = input(question_text).lower()

        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer
        else:
            print("Please answer yes or no")


def strip_string(string):
    return "".join(string.rstrip().lstrip())


# Game for score
def game_start(last_q, score, name):
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
    question = str(random.randint(1, 10))
    while question == last_q:
        # used while instead of if because of the chance of duplicates
        question = str(random.randint(1, 10))
    answer = strip_string(input(f"What is {te_reo_numbers[question]}"))
    if answer == question:  # correct
        score += 1
        print(correct[random.randint(1, 4)])
        last_q = question
        time.sleep(0.4)
        game_start(last_q, score, name)
    else:  # incorrect
        print(f"{incorrect[random.randint(1, 2)]} You're score was: {score} points")
        scoreboard(score, name)
        # no need for int checker, it will be wrong either way.
        # from here send to score board.


def scoreboard(score, name):
    print("Your score has been sent!")
    date = datetime.datetime.now()
    filenum = 1
    f = open(f"{filenum}th.txt", "r")
    if f.read() == "Empty":
        f = open(f"{filenum}th.txt", "w")
        f.write(f"{score}")
        f = open(f"{filenum}th.txt", "a")
        f.write(f' - {name} - {date.strftime("%c")}')
    else:
        if filenum > 5:
            return  # send to replay func
        filenum += 1
        scoreboard(score, name)


game_start(0, 0, "nikki")

# very broken atm
