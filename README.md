**The Fruit Rage!**

A game that captures the nature of a zero sum two player game with strict limitation on allocated time for reasoning.

The Fruit Rage is a two player game in which each player tries to maximize his/her share from a batchof fruitsrandomly placed in a box. The box is divided into cells and each cell is either empty or filled with one fruit of a specific type.

The overall score of each player is the sum of rewards gained for every turn. The game will terminate when there is no fruit left in the boxor when a player has run out of time.

**Goal**
The goal is to develop an AI agent based on Alpha Beta Prunning that  chooses the cell from the game board and that move help agent to earn the maximum score.

**Input Specifications**

*First line:* integer n, the width and height of the square board (0 < n < 26) 
*Second line:* integer p, the number of fruit types (0 < p < 9) 
*Third line:* strictly positive floating point number, your remaining time in seconds 
*Next n lines:* the n x n board, with one board row per input file line, and n characters (plus endof-line marker) on each line. Each character can be either a digit from 0 to p-1, or a * to denote an empty cell.
