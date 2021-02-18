This project implements an algorithm to solve a 8-puzzle using the A* algorithm. 
It uses a Heuristic function (a function saying how far away it is from the correct solution)
and uses breadt-first search to find the quickest solution to solve the puzzle. 
It always starts with a random configuration for the 8-puzzle, so there
is a new 8-puzzle being solved for each time. Not all random configurations of 8-puzzles
can be solved, so it checks after having made the random board configuration
if it solvable or not, and makes a new random board until it has made a board
that is solvable.

I did this project soon after having completed IN1010 - Introduction to java and object oriented programming
at University of Oslo. I read a lot about AI at the time and the A* algorithm I
implemented here after having read about it in a book about AI algorithms.

to run the program it needs to be compiled first, which can be done with
the following command:

>javac *.java

After that the program can be run with the following command:

>java Test