"""
This is a place for me to mess around with file handling in python. (Ignore)
"""
import datetime

file = 1
fixed_score = 999999


def nudger(filenum, score, name):  # this is to push places down
    date = datetime.datetime.now()
    f = open(f"{filenum}th.txt", "r")
    old_1 = int(f.read()[:6])
    filenum += 1
    f = open(f"{filenum}th.txt", "r")
    old_2 = int(f.read()[:6])
    # how will i make the scores better?
    if score >= old_1:
        print("replacing 1st")
        filenum = 1
        # save old 1
        f = open(f"{filenum}th.txt", "r")
        previous = f.read()
        # replace
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
    elif score >= old_2:
        print("replacing 2nd")
        filenum = 2
        # save old 2
        f = open(f"{filenum}th.txt", "r")
        previous = f.read()
        # replace
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
    else:
        print("replacing 3rd")
        filenum = 3
        # replace
        score_nudge = 6 - len(str(score))
        for i in range(score_nudge):
            score = "0" + str(score)
        f = open(f"{filenum}th.txt", "w")
        f.write(f"{score}")
        f = open(f"{filenum}th.txt", "a")
        f.write(f' - {name} - {date.strftime("%c")}')


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


def resetboard():
    delete_board = yes_no("Do you really want to delete the score board? (y/n)")
    filenum = 1
    if delete_board == "Yes":
        while filenum < 4:
            f = open(f"{filenum}th.txt", "w")
            f.write("000000 - No Score")
            filenum += 1


resetboard()
nudger(1, 72, "puppy")
nudger(1, 90, "tree")
nudger(1, 50000, "name")
