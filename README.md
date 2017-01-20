# undirected-graph-kata

## Overview
A program that takes as it's input the edges of an undirected graph and
provides the number of disconnected sub-graphs.

## Details
To input a graph, a user would type "a b b c c a d e". This represents the
edges (a, b) (b, c) (c, a) (d, e). The output of the program would be 2
since there are two distinct disconnected subgraphs. The program continues
prompting the user for an additional graph until exiting.

## Installation
```
python3 setup.py install
```

## Tests
```
python3 setup.py test
```
