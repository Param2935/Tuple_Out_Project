# this file contains the main code for the game

import os 
import sys

# import fucntion definations from module
from tuple_out_module import roll_dice, get_fixed_dice, calculate_score, is_tuple_out, get_players


print("* * * * * TUPLE OUT: The Dice Game! * * * * * *\n")
print("Get the highest score or get to 50 first to WIN!\n")


num_players = get_players()
scores = [0] * num_players
max_score = 50  # score to win

# main loop for the game

while all(score < max_score for score in scores):
        for player in range(num_players):
            print(f"\nPlayer {player + 1}'s turn!")
            dice_rolls = roll_dice()
            print(f"Initial roll: {dice_rolls}")
            
            # Handle "tuple out"
            if is_tuple_out(dice_rolls):
                print("Oh no! You 'tupled out' and scored 0 points this turn.")
                continue
