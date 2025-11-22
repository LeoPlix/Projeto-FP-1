# MNK — Board Game (Tic‑Tac‑Toe Variant)

A Python implementation of the MNK game (a generalization of tic‑tac‑toe). Play against the computer with three difficulty levels. Developed as part of an academic Programming Fundamentals project.

---

## Table of Contents
- Overview
- Features
- Project structure
- Main functions
- AI difficulty levels
- How to run
- Game rules
- Example run
- Requirements
- Contributing
- Author

---

## Overview
The objective is to align K pieces in a row (horizontal, vertical, or diagonal) on an M×N board. A human player competes against an AI-controlled opponent. The player who uses symbol `X` always goes first.

---

## Features
- Configurable board size: M x N and target K
- Three AI difficulty levels: Easy, Normal, Hard
- Automatic detection of wins, losses, and draws
- Text-based interface for the terminal
- Player vs Computer mode

---

## Project structure
The repository contains a single main script:
- `FP2425P1.py` — full implementation of the game, including the functions listed below.

Main functions
- `eh_tabuleiro()` — validates the board structure
- `tabuleiro_para_str()` — converts the board into a string visual representation
- `jogo_mnk()` — main function that starts and runs the game
- `escolhe_posicao_manual()` — handles the user's move input
- `escolhe_posicao_auto()` — implements the computer AI

---

## AI difficulty levels
- Easy: Chooses moves adjacent to its own pieces (simple heuristic).
- Normal: Blocks opponent's immediate winning moves and tries to create winning sequences.
- Hard: Simulates future moves to make more strategic decisions (deeper analysis).

---

## How to run
1. Make sure you have Python 3 installed.
2. Run the script from a terminal:
```bash
python FP2425P1.py
```
During execution the program will ask for:
- Board dimensions: M, N and K
- Player symbol: `X` or `O`
- Computer difficulty level: `Easy`, `Normal` or `Hard`

---

## Game rules
- A player wins by aligning K consecutive pieces horizontally, vertically, or diagonally.
- The game ends when one player wins or when the board is full (draw).
- The player using `X` moves first.

---

## Example run
Example terminal output:
```text
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
```
When prompted, enter the number corresponding to a free cell.

---

## Requirements
- Python 3.x
- No external libraries required

---

## Contributing
Contributions are welcome — bug fixes, AI improvements, refactoring, or additional tests. If you'd like, I can:
- Split the single script into modules (for example `board.py`, `ai.py`, `cli.py`)
- Add unit tests
- Improve documentation with more examples

Tell me which option(s) you prefer and I can prepare changes or a patch.

---

## Author
Developed as part of an academic Programming Fundamentals assignment.
