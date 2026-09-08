# Top K Frequent Elements

## 💡 Overview & Approach
The problem is solved by first calculating the frequency of each element using a hash map (Python's `collections.Counter`). This step takes linear time relative to the number of elements in the input list.

To efficiently identify the top `k` elements, we utilize a **Min-Heap** of size `k`. By iterating through the frequency map and pushing elements into the heap, we ensure that the heap always contains the `k` elements with the highest frequencies seen so far. If the heap size exceeds `k`, we pop the element with the smallest frequency. This approach is more memory-efficient than sorting the entire frequency map, especially when `k` is significantly smaller than the number of unique elements.

## 📊 Complexity Analysis
- **Time Complexity**: **O(N log k)**, where N is the number of elements in the array. Counting frequencies takes O(N), and maintaining a heap of size k takes O(N log k).
- **Space Complexity**: **O(N)**, as we store the frequency of each unique element in a hash map, which in the worst case (all elements unique) is O(N).

## 🏢 Top Companies Asking This Problem
- Google
- Amazon
- Meta
- Microsoft
- Apple
- Uber
- Netflix

## 🚀 Key Features & Edge Cases Handled
- **Small k**: The algorithm handles cases where `k=1` or `k=len(nums)` correctly.
- **Uniform Frequencies**: If all elements have the same frequency, the heap maintains any `k` elements, which satisfies the problem requirements.
- **Memory Efficiency**: By using a heap of size `k` rather than sorting the entire frequency dictionary, we optimize for scenarios where the number of unique elements is very large.
- **Empty Input**: While constraints usually imply `k >= 1`, the logic naturally handles standard input sizes effectively.