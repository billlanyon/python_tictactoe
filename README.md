### Goal
TTT is a repository of a tic tac toe game being built in python from the ground up.
The goal of this project is to educate the builder in test-driven object-oriented development.

Pytest and Travis are testing, Bill Lanyon is learning, and Basil Bibi is kindly mentoring.

[![Build Status](https://travis-ci.org/billlanyon/TTT.svg?branch=develop)](https://travis-ci.org/billlanyon/TTT)

billlanyon@me.com

### How to play
1. Open a terminal session on your computer.
2. Navigate to the downloaded TicTacToe folder your computer.
3. Make the game executable by entering 'chmod +x main.py'
4. Launch the game by entering 'python3 main.py' and following the on screen instructions.
5. Start a game by entering 'y'.
6. Select a board size, from 3 - 9, by entering the dimension in letters, 'six' for example. The default board size is 3x3.
7. Select to play a game against a computer opponent by entering 'c', or 'h' to play against another human.
8. Player X always plays first and a human player always plays first.
9. Enter a two coordinates separated by a space for each move eg. '2 1'.

### Principal classes
Tictactoe, TictactoeMove

### Assumptions
Players must enter accurate input as requested.

### External dependencies
TBC

### Logging
Logging is configured by the file log.conf. Debug messages are currently logged to the file ttt.log and critical messages and above to the console.
