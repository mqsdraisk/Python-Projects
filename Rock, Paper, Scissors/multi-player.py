
#creating a function to calculate wins and losses:
def gameWin(player1, player2):
    if player1==player2:
        return None
    
    elif player1 == "r":
        if player2 == "p":
            return True
        elif player2 == "s":
            return False
        
    elif player1 == "p":
        if player2 == "s":
            return True
        elif player2 == "r":
            return False
    
    elif player1 == "s":
        if player2 == "r":
            return True
        elif player2 == "p":
            return False
        
#players input:
player1 = input("Player 1 choose your Move: Rock(r), Paper(p), Scissors(s): ")
player2 = input("Player 2 choose your Move: Rock(r), Paper(p), Scissors(s): ")

print(f"Player 1 choosed: {player1}\nPlayer 2 choosed: {player2}")
game = gameWin(player1, player2)

#deciding player wins and loss:
if game == None:
    print("The game is a Tie!")
elif game:
    print("Player 2 won the game.")
else: 
    print("Player 1 won the game.")