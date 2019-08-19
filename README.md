# The Task
Knight’s path

Implement a program that finds the shortest path a knight can take between two points on a standard 8x8 chessboard.
In chess, knights move in an L-shape: 2 squares along one dimension, 1 square along the other.
[More details](https://docs.google.com/document/d/1rxSx_MklLEA7zGeMDRrRm1wlBETQVDsvEaf5lnCJoY0/edit#)

# Functional Requirements
Write a command-line executable that reads instructions from standard input (stdin).
Instructions are lines (separated by newlines) in the following format:

**D4 G7**

**D4 D5**

The first of the space-separated values is the knight's starting position, the second is the knight's target position.
For each line in the input, your program should print (to standard out) the shortest path it found. So for the example above, it should print e.g.:

**D4 F5 G7**

**D4 E2 F4 D5**

# Assumptions
* Python 3 is installed
* Board size is 8 x 8
* Invalid input will result in error message
* Lowercase input is converted to uppercase
* Enter exit to stop execution

# Installation
1. Download and install latest Python 3 from [here](https://www.python.org/downloads/)
1. Clone this repository to your local folder

# How to run
1. Open Unix shell and cd to project folder
1. Execute command: ```python knight.py```
