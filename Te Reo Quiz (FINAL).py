"""
This is the final project and it is a Te Reo quiz aimed at children.
"""
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


def game_start(last_question, score):
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
        1: "Nice!",
        2: "Awesome!",
        3: "Great!",
        4: "Better than mama!"
    }
    incorrect = {
        1: "Nice try!",
        2: "Almost, but not quite!"
    }
    # game proper
    question = str(random.randint(1, 10))
    while question == last_question:  # to avoid duplicates
        # used while instead of if because of the chance of duplicates
        question = str(random.randint(1, 10))
    answer = strip_string(input(f"What is {te_reo_numbers[question]}"))
    if answer == question:  # correct
        score += 1  # add score
        print(correct[random.randint(1, 4)])  # produce a reply
        last_question = question  # using this as a way to check duplicates
        time.sleep(0.4)
        game_start(last_question, score)
    elif answer == "reset":  # for resetting
        reset_board()
    else:  # incorrect
        print(f"{incorrect[random.randint(1, 2)]} You're score was: {score} points")
        scoreboard(1, score)
        # no need for int checker, it will be wrong either way.
        # from here send to score board.


def scoreboard(filenum, score):  # this is to push places down i.e. take first place to second when overtaken
    name = input("What name do you want your score to be under? :")
    date = datetime.datetime.now()
    # saving previous 1st-3rd places for comparison
    f = open(f"{filenum}th.txt", "r")
    old_1 = int(f.read()[:6])
    filenum += 1
    f = open(f"{filenum}th.txt", "r")
    old_2 = int(f.read()[:6])
    filenum += 1
    f = open(f"{filenum}th.txt", "r")
    old_3 = int(f.read()[:6])
    # if score is bigger than 1st
    if score >= old_1:
        print("You are 1st on the leader board!")
        filenum = 1
        # save old 1
        f = open(f"{filenum}th.txt", "r")
        previous = f.read()
        # replace with new score
        score_nudge = 6 - len(str(score))
        for i in range(score_nudge):
            score = "0" + str(score)
        f = open(f"{filenum}th.txt", "w")
        f.write(f"{score}")
        f = open(f"{filenum}th.txt", "a")
        f.write(f' - {name} - {date.strftime("%c")}')
        # save old 2
        filenum += 1
        f = open(f"{filenum}th.txt", "r")
        previous2 = f.read()
        # replace
        f = open(f"{filenum}th.txt", "w")
        f.write(f"{previous}")
        filenum += 1
        # replace 3rd (does not need to be saved)
        f = open(f"{filenum}th.txt", "w")
        f.write(f"{previous2}")
        f.close()
    # if score is bigger than 2nd
    elif score >= old_2:
        print("You are 2nd on the leader board!")
        filenum = 2
        # save old 2
        f = open(f"{filenum}th.txt", "r")
        previous = f.read()
        # replace with new score
        score_nudge = 6 - len(str(score))
        for i in range(score_nudge):
            score = "0" + str(score)
        f = open(f"{filenum}th.txt", "w")
        f.write(f"{score}")
        f = open(f"{filenum}th.txt", "a")
        f.write(f' - {name} - {date.strftime("%c")}')
        # replace 3rd (does not need to be saved)
        filenum += 1
        f = open(f"{filenum}th.txt", "w")
        f.write(f"{previous}")
        f.close()
    # if score is bigger than 3rd
    elif score >= old_3:
        print("You are 3rd on the leader board!")
        filenum = 3
        # replace with new score
        score_nudge = 6 - len(str(score))
        for i in range(score_nudge):
            score = "0" + str(score)
        f = open(f"{filenum}th.txt", "w")
        f.write(f"{score}")
        f = open(f"{filenum}th.txt", "a")
        f.write(f' - {name} - {date.strftime("%c")}')
        f.close()
    print("loading scoreboard...")
    time.sleep(2)
    print("Score - Name - Time/Date")
    show_scores()


def show_scores():
    file = 1
    while file < 4:  # reads the file and displays it.
        f = open(f"{file}th.txt", "r")
        print(f.read())
        time.sleep(0.4)
        file += 1
        f.close()
    # ask if they want to replay
    replay = yes_no("Would you like to play again? (y/n)")
    if replay == "Yes":
        game_start(0, 0)
    else:
        print("Thanks for playing!")


def reset_board():
    # reset board
    delete_board = yes_no("Do you really want to delete the score board? (y/n)")
    filenum = 1
    if delete_board == "Yes":
        while filenum < 4:
            # replaces all places with the default 000000 - No Score
            f = open(f"{filenum}th.txt", "w")
            f.write("000000 - No Score")
            filenum += 1
        print("Reset Complete")


# Main
print("Welcome to the Te Reo Counting Quiz!\n"
      "*clapping sounds*")
time.sleep(0.6)
print(f"Welcome to the Show!\n")
show_instructions = yes_no("Have you played before? ")  # ask if they have played before
if show_instructions == "No":
    time.sleep(0.5)
    # printing rules
    print("OK! I hope you brushed up on your Te Reo skills, this will be a Quiz!\n"
          "The rules of the game:\n"
          "There will be a word that pops up on your screen\n"
          "Just type the number that corresponds to that number and just need to type it out and press enter!")
time.sleep(0.8)
print("Hope you're ready!\n"
      "Lets go!")
time.sleep(1.4)
game_start(0, 0)  # starting the game
