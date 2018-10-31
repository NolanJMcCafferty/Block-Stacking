# Block-Stacking Dynammic Programming Algorithm
### Nolan McCafferty and Michele Pashby
CS140 Algorithms Homework 9 Problem 3, Due 10/31/18


## Instructions
To run our file in Terminal:
```
$python max_height.py inputFile.in outputFile.out
```

## Contents of our repository:
README.md   - README file explaining the contents of our repository and our algorithm
max_height.py  -the file where our algorithm is coded, when compiled will produce the solution
infile.txt  -sample input file where we got input to test our algorithm
output.txt  -output file where we output the result of our algorithm based on the sample input

## Our Algorithm
Our algorithm works by first creating an array of all the possible rotations of the box types,
and then sorts them by base area in decreasing order. Then, for each box, it creates potential
stacks by comparing itself with boxes with larger areas, and then computing the max height for each
of the possible outcomes. This in turn gives us an array of maximum heights for a given stack
starting with block k. We then select the maximum of these values, and retrieve the corresponding
order of blocks, which is the optimal solution.

## Design Choice
One interesting design decision we made was to sort the block types by the area of their bases,
and then to only compare a box to those of bigger areas. This saves some time, since each box does
not need n comparisons. We considered not doing this, but decided to implement it to save time in
the comparisons.

## Running Time and Space Complexities
Our algorithm has a running time of O(n^2) because for each possible block k,
it is compared against all the blocks with a bigger area, which at the very most when block k
is the smallest, has n comparisons. Therefore, there are at most n x n operations, meaning
it is compared against all n blocks, so the upper bound is n squared operations.

The algorithm that we created takes up Theta(n) space because the dynamic programming table
we have is a one dimensional array containing n elements given an input of n blocks.

## Testing the Code
We tested our code using the sample files on Piazza as well as some of our own examples.
Our results were identical to those in the sample output files.
