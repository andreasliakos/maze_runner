# maze_runner

1 Introduction

An interesting problem is the design of labyrinths. In this paper we are asked to create
mazes using the structure of disjoint sets. Then we are asked to draw the path from the entrance
to the exit of the maze using the Breadth First Search algorithm.

2 Problem description

The maze can be viewed as an M × N grid consisting of cells with each cell having 4 sides
with some of them possibly open. The cells on the periphery of the grid have closed sides to
the outside, except for the 2 cells that will be the entrance to and exit from the maze. A valid
maze should have an entrance and an exit as well as a path leading from the entrance to the
exit through open sides between cells. The writing of programs is requested.
that performs the following a) maze creation b) maze design and c) tracking and path design
from the entrance to the exit.

2.1 Creating a maze

A maze will be created using the disjoint sets structure taking as input the dimensions of
the grid (width and height), the entry position and the exit position. The entry position will be
determined by the outer side of the maze (U=up, D=down, L=left, R=right) and the row or
column in which it is located. Similarly for the exit position. 

Maze creation algorithm

Let S be a set of sets of connected cells. Initially each cell is also a distinct set and S is
{{1}, {2}, {3}, ...}. Moreover, let E be the set of edges representing the neighborhood of
each cell. For example, in the labyrinth of the figure
1, for cell 1 these edges are (1,2) and (1,5), while for cell 7 the edges defining its neighbouring
cells are (7,3), (7,6), (7,8) and (7,11). Algorithm 1 takes as input
the sets S and E and describes the process of creating a labyrinth using foreign
sets.

![image](https://user-images.githubusercontent.com/115406856/220788131-9418d438-51ad-4312-96d5-c9ac5d7dd277.png)

2.2 Maze design

The maze will be drawn either on the console using ASCII characters, or graphically (e.g.
using the matplotlib or other graphics library). Indicative forms of the maze are shown in
Figure 2.

![image](https://user-images.githubusercontent.com/115406856/220788380-f90ef590-f6df-4d01-93b9-191f1ec9bf89.png)

2.3 Tracing the route from the entrance to the exit

Implement the search algorithm first along the width so that it locates and plots the path
from the entrance to the exit of the maze. Optionally, implement additional search algorithms.
