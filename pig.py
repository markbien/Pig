import random

def roll():
    min_value = 1
    max_value = 6

    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    
    if players.isdigit():
        players = int(players)
        #if 1 <= players and players <= 4:
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 1 - 4 players.")
    else:
        print("Invalid input, please try again.")

print(players)