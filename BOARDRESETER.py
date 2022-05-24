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
        while filenum < 3:
            f = open(f"{filenum}nt.txt", "w")
            f.write("")
