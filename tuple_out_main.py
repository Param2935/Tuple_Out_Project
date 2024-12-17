# this file contains the main code for the game

import os 
import sys
import time
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

# import fucntion definations from module
from tuple_out_module import roll_dice, get_fixed_dice, calculate_score, is_tuple_out, get_players


print("* * * * * TUPLE OUT: The Dice Game! * * * * * *\n")
print("Get the highest score or get to 50 first to WIN!\n")

# to track player score 
num_players = get_players()
scores = [0] * num_players
win_score = 50  # score to win
game_over = False  # to print the game over message

# store total time per player 
player_time = [0] * num_players  

# track score
score_track = { [] for i in range(num_players)}



# main loop for the game

while all(score < win_score for score in scores):
        for player in range(num_players):
            print(f"\nPlayer {player + 1}'s turn")
            dice_rolls = roll_dice()
            print(f"Initial roll: {dice_rolls}")
            
            # Handle "tuple out"
            if is_tuple_out(dice_rolls):
                print("Whoops! That's a tuple put :( you score 0 this round.")
                continue

            # loop for re-rolling 
            while True:
                fixed_indices = get_fixed_dice(dice_rolls)
                print(f"Fixed dice: {[dice_rolls[i] for i in fixed_indices]}")

                # Determine dice to re-roll
                re_roll_indices = [
                    i for i in range(len(dice_rolls)) if i not in fixed_indices
                ]
                
                if not re_roll_indices:
                    print("No dice to re-roll.")
                    break
                
                re_roll_choice = input(
                    f"Would you liek to re-roll these dices {re_roll_indices}? (yes/no): "
                ).strip().lower()
                
                if re_roll_choice == "yes":
                    for i in re_roll_indices:
                        dice_rolls[i] = roll_dice(1)[0]
                    print(f"New roll: {dice_rolls}")
                    
                    if is_tuple_out(dice_rolls):
                        print("Whoops! That's a tuple put :( you score 0 this round.")
                        break
                else:
                    break

             # End turn scoring
            if not is_tuple_out(dice_rolls):
                turn_score = calculate_score(dice_rolls)
                scores[player] += turn_score
                print(f"Player {player + 1} scored {turn_score} points this turn.")
                print(f"Total score: {scores[player]}")
            
            # Check for a winner
            if scores[player] >= win_score:
                print(f"\nLESSGO! Player {player + 1} won with final score of {scores[player]}")
                game_over = True
                break    # to exit the loop after win
    
print("\nGame over!")

