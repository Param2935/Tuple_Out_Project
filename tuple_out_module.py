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

# Function for choosing game mode
def get_game_settings():
    print("\nChoose Game Mode:")
    print("1. Default Mode (Highest score or first to 50 wins)")
    print("2. Custom Mode (Set your own winning score or maximum rounds)")
    
    while True:
        choice = input("Enter D for Default or C for Custom: ").strip()
        if choice == "D":
            return {"win_score": 50, "max_rounds": None}  # default settings
        elif choice == "C":
            win_score = None
            max_rounds = None

            # get custom winning score
            while True:
                try:
                    win_score = int(input("Enter the winning score: "))
                    if win_score > 0:
                        break
                    else:
                        print("Winning score must be greater than 0.")
                except ValueError:
                    print("Please enter a valid number.")

            # get maximum rounds
            while True:
                try:
                    max_rounds = int(input("Enter the maximum number of rounds: ").strip())
                    if max_rounds > 0:
                        break
                    else:
                        print("Number of rounds must be greater than 0.")
                except ValueError:
                    print("Please enter a valid number.")
            
            return {"win_score": win_score, "max_rounds": max_rounds}
        else:
            print("Invalid choice. Please enter D or C.")