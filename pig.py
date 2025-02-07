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

MAX_SCORE = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < MAX_SCORE:

    for i in range(players):
        print("\nPlayer", i + 1, "turn has just started!\n")
        print("Your current score is:", player_scores[i],"\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score for this turn is:", current_score,"\n")

        player_scores[i] += current_score
        print("Your total score is:", player_scores[i],"\n")

WINNING_SCORE = max(player_scores)
WINNING_INDEX = player_scores.index(WINNING_SCORE)

print("Player", WINNING_INDEX+1, "is the winner with a score of:", WINNING_SCORE)
