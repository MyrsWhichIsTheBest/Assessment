import time


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


print("Welcome to the Te Reo Counting Quiz!\n"
      "*clapping sounds*")
time.sleep(0.6)
print(f"Welcome to the Show!\n")
show_instructions = yes_no("Have you played before? ")
if show_instructions == "No":
    time.sleep(0.5)
    print("OK! I hope you brushed up on your Te Reo skills, this will be a Quiz!\n"
          "The rules of the game:\n"
          "There will be a word that pops up on your screen\n"
          "Just type the number that corresponds to that number and just need to type it out and press enter!")
time.sleep(0.8)
print("Hope you're ready!\n"
      "Lets go!")
time.sleep(1.4)

