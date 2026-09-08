# Longest Consecutive Sequence

## 💡 Overview & Approach
The problem requires finding the longest sequence of consecutive integers in an unsorted array. A naive approach would involve sorting the array, which takes O(N log N) time. To achieve an optimal O(N) time complexity, we utilize a **Hash Set** to store all unique elements from the input.

The core intuition is to identify the "start" of a sequence. A number `x` is the start of a sequence if `x - 1` is not present in the set. Once a start is identified, we iterate forward (`x + 1`, `x + 2`, ...) to count the length of that specific sequence. Because we only initiate the counting process from the start of a sequence, each element in the array is visited at most twice (once during the initial set insertion and once during the sequence traversal), ensuring linear time performance.

## 📊 Complexity Analysis
- **Time Complexity**: O(N), where N is the number of elements in the input array. Although there is a nested `while` loop, each element is visited at most twice across the entire execution.
- **Space Complexity**: O(N), as we store all unique elements of the input array in a hash set.

## 🏢 Top Companies Asking This Problem
- Google
- Amazon
- Meta
- Microsoft
- Bloomberg
- Adobe

## 🚀 Key Features & Edge Cases Handled
- **Empty Input**: Returns 0 correctly if the input list is empty.
- **Duplicates**: The use of a `set` automatically handles duplicate numbers, ensuring they do not interfere with sequence counting.
- **Single Element**: Correctly identifies a sequence length of 1 for arrays with one element.
- **Non-consecutive sequences**: Efficiently skips numbers that are not the start of a sequence, maintaining the O(N) performance constraint.