# Tuple Out Game Guide

Introduction:
Tuple Out is a dice-based game where players compete to reach the target score of 50 points first or achieve the highest score. Each turn, players roll dice, fix certain dice to keep their scores, and re-roll others to maximize their score. However, beware of 'tuple out' rolls, which score 0 points for the round. The game dynamically tracks scores, and the first player to reach or exceed 50 wins.
 
How to Play:
Run the Program: Use Python to execute the program file (tuple_out_main.py). Make sure you have the helper module (tuple_out_module.py) in the same directory.

Game Instructions:
After launching the program, follow the prompts to input the number of players
The game will alternate turns among the players, displaying dice rolls and scores.

Gameplay:
Initial Roll: Each player rolls 5 dice at the start of their turn.
Fix Dice: Players can fix certain dice and re-roll others to improve their score.
Re-Rolls: Continue re-rolling until satisfied with the roll or no dice remain for re-rolling.
Score Calculation: The final dice configuration determines the player's score for the round.
"Tuple Out" Rule: If the dice roll contains a tuple the player scores 0 points for that turn.
Winning: The game ends immediately when one player reaches or exceeds 50 points, and the winner is declared.

Example Gameplay:
Sample Commands and Outputs:

The program asks for the number of players:

Enter the number of players: 3
Player rolls are displayed:


Player 1's turn
Initial roll: [2, 5, 5, 1, 3]
After fixing and re-rolling, the score is calculated:

Player 1 scored 12 points this turn.
Total score: 35

When a player reaches or exceeds 50 points, the winner is declared:
LESSGO! Player 2 won with a final score of 52!

The program displays:
Game over!


Speacial Features:

#1 Time Tracking
This is feture added to the final project trackes the time taken by a player in their turn. At the end of the game, it will display the total time taken by a player in all of their turns. The clock start when the intital roll and stops when the player's turn end. The program will record this time and keep adding time taken for each turn. After the game is over it will display the total time taken by (each) player in their turn(s).

#2 Data Visualization 
This special feature, using Panda, stores the scores of the players after each round and then, using Seaborn, plots a line graph to visualize the player score over each round.




Requirements:
Python version 3.6 or later.

Modules Used: 
os
sys
