import random
question = input("Pick r, p, or s")
options = [ "r", "p", "s"]
computer = random.choice(options)
winner = "you won"
loser = "you lost"

if question == computer:
    print(f"the computer picked {computer})
    print("it's a tie")
elif question == "r" and computer == "p":
    print(f"the computer picked {computer})
    print(winner)
elif question == "r" and computer == "s":
    print(f"the computer picked {computer})
    print(winner)
elif question == "s" and computer == "p":
    print(f"the computer picked {computer})
    print(winner)
elif question == "s" and computer == "r":
    print(f"the computer picked {computer})
    print(loser)
elif question == "p" and computer == "s":
    print(f"the computer picked {computer})
    print(loser)
elif question == "p" and computer == "r":
    print(f"the computer picked {computer})
    print(winner)
else:
    print("didn't work")
