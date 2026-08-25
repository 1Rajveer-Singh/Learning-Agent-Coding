# A* Pathfinding Algorithm

## Language
Java

## Category
General

## Problem
You are given a 2D grid where 0 represents a walkable cell and 1 represents an obstacle. Starting from the top-left cell (0,0), find the minimum number of moves required to reach the bottom-right cell. You may move up, down, left, or right. Implement the A* search algorithm using the Manhattan distance as the heuristic. Return the shortest path length. If the target cannot be reached, return -1.

## Approach
Solved challenge targeting expected complexity: O(n*m*log(n*m)). Constraints: 1<=n<=100, 1<=m<=100, grid[i][j]∈{0,1}, grid[0][0]=0, grid[n-1][m-1]=0

## Complexity
- Time: O(N * M * log(N * M))
- Space: O(N * M)

## Files
- a_pathfinding_algorithm.java: solution source code
- README.md: problem notes and explanation
