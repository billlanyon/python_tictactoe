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
6. Select a game against a computer opponent by entering 'c', or 'h' to play against another human.
7. A human player always plays first: they chose their player by entering X or O, a space, and then a cell from 0 to 8.
   The following players then just enter a coordinate for each move.

### Principal classes
Tictactoe, TictactoeMove

### Assumptions
Players must enter accurate input as requested.

### External dependencies
TBC

### Logging
When launching the app from the command line:<br>
Appending '-d' enables the display of debug messages in the console.<br>
Appending '-f' enables the logging of debug messages to a file named 'ttt.log'.
