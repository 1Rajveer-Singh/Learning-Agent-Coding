# 3Sum

## 💡 Overview & Approach
The problem is solved using the **Sorting + Two-Pointer** technique. First, we sort the input array, which allows us to navigate the search space systematically and handle duplicates easily. Sorting takes $O(N \log N)$ time.

We iterate through the array, treating each element as the "anchor" of a potential triplet. For each anchor, we use two pointers (`left` starting just after the anchor, and `right` at the end of the array) to find two other numbers that sum up to the negative of the anchor. Because the array is sorted, if the current sum is too small, we increment the `left` pointer; if it is too large, we decrement the `right` pointer. This reduces the search for the remaining two numbers from $O(N^2)$ to $O(N)$ for each anchor.

## 📊 Complexity Analysis
- **Time Complexity**: $O(N^2)$, where $N$ is the length of the array. The sorting step takes $O(N \log N)$, and the nested loop structure (the outer loop runs $N$ times, and the two-pointer inner loop runs $O(N)$ times) dominates the complexity.
- **Space Complexity**: $O(1)$ or $O(N)$ depending on the implementation of the sorting algorithm (Python's Timsort uses $O(N)$ space). We do not use any additional data structures that scale with input size, excluding the output list.

## 🏢 Top Companies Asking This Problem
- Google
- Amazon
- Meta
- Microsoft
- Apple
- Bloomberg
- Adobe

## 🚀 Key Features & Edge Cases Handled
- **Duplicate Triplets**: The algorithm explicitly skips duplicate values for the anchor, `left`, and `right` pointers to ensure the result contains only unique triplets.
- **Empty/Small Arrays**: The loop range `n - 2` naturally handles cases where the array has fewer than 3 elements, returning an empty list.
- **Positive Sum Optimization**: If the anchor element is greater than 0, the loop terminates early because it is impossible to form a zero-sum triplet with sorted positive numbers.
- **All Zeros**: Correctly identifies `[0, 0, 0]` as a valid triplet if three or more zeros exist in the input.