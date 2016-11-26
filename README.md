# undirected-graph-kata

## Overview
This program takes as it's input the edges of an undirected graph and
prints the number of disconnected sub-graphs.

To run the automated tests use `python3 setup.py tests`.
For package installation run `python3 setup.py install`.

## Details
To input a graph, a user would type "1 2 2 3 3 1 4 5". This represents the
edges (1, 2) (2, 3) (3, 1) (4, 5). The output of the program at this time would
be 2 since there are two distinct disconnected subgraphs. The component
continues taking inputs so if the user would then type "2 5" then the program
outputs 1 because a connection between the two subgraphs has been made.

## Implementation
