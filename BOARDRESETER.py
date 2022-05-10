def resetboard():
    delete_board = input("Do you really want to delete the score board? (y/n)")
    filenum = 1
    f = open(f"{filenum}nt.txt", "w")
    f.write("Empty")
