# This file contains some function definations to be used by the main code

import random

# Function to roll dice
def roll_dice(num_dice = 3):
    
    return [random.randint(1, 6) for _ in range(num_dice)]


# Function to check for tuple out
def is_tuple_out(dice_rolls):
    
    return len(set(dice_rolls)) == 1

# Function to get fixed dice
def get_fixed_dice(dice_rolls):
    
    fixed = []
    for i, value in enumerate(dice_rolls):
        if dice_rolls.count(value) == 2:
            fixed.append(i)
    return fixed


# Function to calculate the score
def calculate_score(dice_rolls):
   
    return sum(dice_rolls)

#Function for user input for all the number of players
def get_players():
    while True:
        try: 
            num_players = int(input("Please enter the number of players playing:"))
            if num_players > 0:
                return num_players
            else: 
                print("ERROR! Players must be at least 1. Try again.")
        except ValueError:
            print("ERROR! Please enter a valid integer.")