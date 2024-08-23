import random

# creating a function to decide wins:
def gameWin(computer, player):
    if computer==player:
        return None
    elif computer == "r":
        if player == "p":
            return True
        elif player == "s":
            return False
    elif computer == "p":
        if player == "r":
            return False
        elif player == "s":
            return True
    elif computer == "s":
        if player == "r":
            return True
        elif player == "p":
            return False

# Defining player and computer
print("Computer is choosing it's move...")

#using random module to randomly choose moves as numbers:
randomNo = random.randint(1,3)

if randomNo == 1:
    computer = "r"
elif randomNo == 2:
    computer = "p"
elif randomNo == 3:
    computer = "s"

player = input("Choose your move: Rock(r), Scissors(s), Paper(p): ")

print(f"The computer choosed: {computer}\nYou choosed: {player}")
game = gameWin(computer, player)

#deciding the game winning
if game == None:
    print("The game is a Tie!")
elif game:
    print("Congratulations, You Won the Game!")
else:
    print("Better luck next time! you played well.")