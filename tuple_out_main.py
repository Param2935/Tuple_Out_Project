# this file contains the main code for the game

import os 
import sys
import csv
import time
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

# import fucntion definations from module
from tuple_out_module import roll_dice, get_fixed_dice, calculate_score, is_tuple_out, get_players, get_game_mode


print("* * * * * TUPLE OUT: The Dice Game! * * * * * *\n")
print("Get the highest score or get to 50 first to WIN!\n")

# to track player score 
num_players = get_players()
scores = [0] * num_players
game_settings = get_game_mode()
win_score = game_settings["win_score"]
max_rounds = game_settings["max_rounds"]
game_over = False  # to print the game over message

round_counter = 0   # track the number of rounds

# store total time per player 
player_time = [0] * num_players  

# track score
score_data = {f"Player {i+1}": [] for i in range(num_players)}

current_round = 1

# main loop for the game
while all(score < win_score for score in scores and (max_rounds is None or current_round <= max_rounds)::
        for player in range(num_players):
            print(f"\nPlayer {player + 1}'s turn")
            
            # start time tracking
            start_time = time.time()

            dice_rolls = roll_dice()
            print(f"Initial roll: {dice_rolls}")
            
            # Handle "tuple out"
            if is_tuple_out(dice_rolls):
                print("Whoops! That's a tuple put :( you score 0 this round.")
                # store data score
                score_data[f"Player {player+1}"].append(scores[player]) 
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
                    f"Would you like to re-roll these dices {re_roll_indices}? (yes/no): "
                ).strip().lower()
                
                if re_roll_choice == "yes":
                    for i in re_roll_indices:
                        dice_rolls[i] = roll_dice(1)[0]
                    print(f"New roll: {dice_rolls}")
                    
                    if is_tuple_out(dice_rolls):
                        print("Whoops! That's a tuple put :( you score 0 this round.")
                        # store data score
                        score_data[f"Player {player+1}"].append(scores[player]) 
                        break
                else:
                    break

             # End turn scoring
            if not is_tuple_out(dice_rolls):
                turn_score = calculate_score(dice_rolls)
                scores[player] += turn_score
                print(f"Player {player + 1} scored {turn_score} points this turn.")
                print(f"Total score: {scores[player]}")
                score_data[f"Player {player+1}"].append(scores[player])

            # Stop timer and record player time
            end_time = time.time()
            time_period = end_time - start_time
            player_time[player] += time_period
            print(f"Time taken for player {player+1}'s turn: {time_period:.2f} seconds")
            
            # Check for a winner
            if scores[player] >= win_score:
                print(f"\nLESSGO! Player {player + 1} won with final score of {scores[player]}")
                game_over = True
                break    # to exit the loop after win
        
        current_round += 1
    
        # Check for max rounds 
        if max_rounds and round_counter >= max_rounds:
          print("\nMaximum rounds reached!")
          game_over = True




print("\nGame over!")
print("\nFinal Scores:")
for i, score in enumerate(scores):
    print(f"Player {i + 1}: {score}")



# display time data at the end
for i, time_taken in enumerate(player_time):
    print(f"Player {i+1} total time: {time_taken:.2f} seconds")



# determine winner in case of max rounds
if not any(score >= win_score for score in scores):
    highest_score = max(scores)
    winners = [i + 1 for i, score in enumerate(scores) if score == highest_score]
    if len(winners) > 1:
        print(f"\nIt's a tie between Players {', '.join(map(str, winners))} with {highest_score} points each!")
    else:
        print(f"\nPlayer {winners[0]} wins with the highest score of {highest_score}!")



# filling missing rounds with the last score so the list are same length
rounds = max(len(scores) for scores in score_data.values())
for player, scores in score_data.items():
    while len(scores) < rounds:
        if scores:
            scores.append(scores[-1]) 
        else:   # start with 0 if the player has no scores
            scores.append(0)



# creating a csv file and first storing data there
csv_file = "score_records.csv"
with open(csv_file, mode="w", newline="") as file:
    writer =  csv.writer(file)
    header = ["Round"] + list(score_data.keys())
    writer.writerow(header)

    # write score data round by round
    for i in range(rounds):
        row = [i + 1] + [score_data[player][i] for player in score_data.keys()]
        writer.writerow(row)


score_df = pd.DataFrame(score_data)
sns.set(style="darkgrid")
plt.figure(figsize=(11,7))


# add 0 as the origin and rounds starting from 1
rounds = list(range(len(score_df) + 1))  # include round 0
for player in score_df.columns:
    sns.lineplot(
        x=rounds,  
        y=[0] + list(score_df[player]),  # add 0 as the starting score
        label=player,
        marker='o',
    )

# plots 
plt.xticks(ticks=rounds)


plt.title("Progess Scoreboard")
plt.xlabel("Round")
plt.ylabel("Score")
plt.legend(title="Players")
plt.show()


