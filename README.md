This project implements the classic MNK game (a tic-tac-toe variant) in Python. The game allows a human player to compete against a computer with three different difficulty levels. The objective is to align a specific number of consecutive pieces (K) on an M x N dimension board.

Features
Customizable Board: Configurable M x N dimensions

Multiple Difficulty Levels: Easy, Normal, and Hard

Verification System: Automatic detection of wins, losses, and draws

Text Interface: Clear board visualization in the terminal

Player vs Computer: Game mode against AI

Project Structure
The project consists of a single Python file (FP2425P1.py) containing all the necessary functions for the game's operation:

Main Functions
eh_tabuleiro() - Validates the board structure

tabuleiro_para_str() - Converts the board to visual representation

jogo_mnk() - Main function that starts the game

escolhe_posicao_manual() - Processes the user's move

escolhe_posicao_auto() - Implements the computer's AI

AI Difficulty Levels
Easy: Plays in positions adjacent to its own pieces

Normal: Blocks opponent's winning moves and tries to create winning sequences

Hard: Uses simulation of future moves to make strategic decisions

How to Run
bash
python FP2425P1.py
During execution, the program will request:

Board dimensions (M, N, K)

Player's symbol (X or O)

Computer's difficulty level

Game Rules
The player who aligns K consecutive pieces (horizontally, vertically, or diagonally) wins

The game ends when a player wins or when the board is full (draw)

The player with 'X' moves first

Usage Example
text
Welcome to MNK GAME.
The player plays with 'X'.
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+

Player's turn. Choose a free position: 5
Requirements
Python 3.x

No external libraries required

Author
Developed as part of an academic Programming Fundamentals project.
