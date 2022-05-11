n-Queens Problem 

Directions: Do this homework BY YOURSELF – without the assistance of others. 

Description: NP-Complete problems are usually solved through brute force (i.e. trying all possible 
combinations). This is horrifically slow, as you’ll soon see. For this assignment, you’ll be coding up one of 
the most famous NP-Complete problems, called the n-Queens problem. If you don’t know how to play 
chess, that’s OK; you only need to know the movements of one piece: the queen. 
A queen can attack another piece along any row, column or diagonal of the square the queen is currently in – 
making her arguably the most powerful piece on the board. So, for example, we imagine that a chess board is 
defined a 2D array of ints (e.g. int chessboard[8][8]). If a queen is in the upper-left of the board (i.e. at 
chessboard [0][0]), she can attack any piece located in row 0 (i.e. chessboard[i][0]) or any column (i.e. 
chessboard[0][i]). Further, she can attack any piece along the diagonal (i.e. chessboard[i][i]). 
In the case of a standard 8x8 chessboard, the challenge is to place 8 queens on the board such that no queen 
can directly attack another. When generalized, the n-Queens problem states that for a nxn chessboard, place 
n-queens on the board so that no queen can attack another queen. 
Your task is to write a program that takes in a single number: the dimensions of the chessboard. The output 
of the program is a configuration of the chessboard that solves for that dimension. 
