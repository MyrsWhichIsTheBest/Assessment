import time


def strip_string(string):
    return "".join(string.rstrip().lstrip())


def yes_no(answer):
    strip_string(answer)
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("Un ")


print("Welcome to the Te Reo Counting Quiz!\n"
      "*clapping sounds*\n"
      "Now time to introduce the contestant for tonight!")
time.sleep(0.4)
name = input("Whats your name?: ")
time.sleep(0.4)
print(f"Welcome, {name}, to the Show!\n")
time.sleep(0.8)
instructions = input("Do you want to read the rules? Its not (too) hard! (Y/N)").lower()

if instructions:
    time.sleep(1)
    print("OK! I hope you brushed up on your Te Reo skills, this will be a Quiz!\n"
          "But first the rules of the game\n"
          "There will be a word that pops up on your screen\n"
          "Just type the number that corresponds to that number and just need to type it out and press enter!")
time.sleep(0.8)
print("Hope you're ready!\n"
      "Lets go!")
time.sleep(1.4)
