import random

chose = ""
draw = "it's a draw"
win = "you won !"
lose = "you lost :("
while (len(chose) == 0 or chose != "r" and chose != "p" and chose != "s"):
    chose = input("Chose rock, paper or scissors (r/p/s)  ")
if chose == "r":
    chose = "rock"
elif chose == "s":
    chose = "scissors"
else:
    chose = "paper"
print("You chosed " + chose)
issues = ["rock", "paper", "scissors"]
rng = random.choice(issues)
print("They chosed " + rng)
if rng == "rock":
    if chose == "rock":
        print(draw)
    elif chose == "scissors":
        print(lose)
    else:
        print(win)
elif rng == "paper":
    if chose == "rock":
        print(lose)
    elif chose == "scissors":
        print(win)
    else:
        print(draw)
else:
    if chose == "scissors":
        print(draw)
    elif chose == "paper":
        print(lose)
    else:
        print(win)


