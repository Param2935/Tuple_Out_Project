# This file contains some function definations to be used by the main code

import random

# Function to roll dice
def roll_dice(num_dice=3):
    
    return [random.randint(1, 6) for _ in range(num_dice)]


# Function to check for "tuple out"
def is_tuple_out(dice_rolls):
    
    return len(set(dice_rolls)) == 1
