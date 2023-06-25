
import random, os

print("Rock, paper, scissors!")

modes = ["a", "b"]
while True:
    mode = input("Choose the mode:\na) 1 Player vs CPU\nb) 2 Player\n")
    if mode not in modes:
        print ("Not a valid option, please try again.")
    else:
        break

print("Chosen mode: {}".format(mode))

options = ["Rock", "Paper", "Scissors"]

while True:
    player_1 = input("Player 1, choose rock(R), paper (P) or scissors (S): ").capitalize()
    if player_1 not in options:
        print ("Not a valid option, please try again.")
    else:
        break

os.system('cls')

if mode == "a":
    player_2 = random.choice(options)
    print("CPU: {}".format(player_2))
else:
    while True:
        player_2 = input("Player 2, choose rock(R), paper (P) or scissors (S): ").capitalize()
        if player_2 not in options:
            print ("Not a valid option, please try again.")
        else:
            break

#os.system('cls')

if player_1 == player_2:
    print("It's a tie!")
elif (player_1 == "Rock" and player_2 == "Scissors") or \
     (player_1 == "Scissors" and player_2 == "Paper") or \
     (player_1 == "Paper" and player_2 == "Rock"):
    print("Player 1 wins!")
else:
    if mode == "a":
        print("CPU wins!")
    else:
        print("Player 2 wins!")