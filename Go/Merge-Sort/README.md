# Merge Sort

## Language
Go

## Category
Arrays

## Problem
Implement a sorting algorithm to arrange elements of an integer array in non-decreasing order using the divide and conquer strategy.

## Approach
The input array is recursively divided into two halves until sub-arrays of size one are reached. These sub-arrays are then merged back together in sorted order by comparing elements from each half and appending the smallest to a result slice.

## Complexity
- Time: O(n log n)
- Space: O(n)

## Files
- merge_sort.go: solution source code
- README.md: problem notes and explanation
