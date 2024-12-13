import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


while True:
    player = input("Enter the number of players (2 - 4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")


max_score = 50
player_score = [0 for _ in range(player)]


while max(player_score) < max_score:
    for player_idx in range(player):
        print(f"\nPlayer number {player_idx + 1}'s turn has just started!")
        print(f"Your total score is: {player_score[player_idx]}\n")
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

            print("Your current score is:", current_score)

     
        player_score[player_idx] += current_score
        print("Your total score is:", player_score[player_idx])


max_score = max(player_score)
winning_idx = player_score.index(max_score)
print(f"\nPlayer number {winning_idx + 1} is the winner with a score of: {max_score}")
