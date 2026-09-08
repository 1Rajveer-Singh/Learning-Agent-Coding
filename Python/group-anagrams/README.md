# Group Anagrams

## 💡 Overview & Approach
The problem requires identifying strings that contain the exact same characters with the same frequencies. The most efficient way to group these is to define a "canonical form" for every string. Since anagrams, when sorted alphabetically, result in the identical string, we use the sorted version of each string as a key in a hash map (dictionary).

We iterate through the input list once, sort each string to generate its key, and append the original string to the corresponding list in our hash map. Finally, we return the values of the hash map, which represent the grouped anagrams. This approach avoids the need for expensive nested comparisons.

## 📊 Complexity Analysis
- **Time Complexity**: O(N * K log K), where N is the number of strings and K is the maximum length of a string. We iterate through N strings, and for each, we perform a sort operation which takes O(K log K).
- **Space Complexity**: O(N * K), as we store all strings in the hash map, where N is the number of strings and K is the average length of the strings.

## 🏢 Top Companies Asking This Problem
- Google
- Amazon
- Meta
- Microsoft
- Uber
- Bloomberg

## 🚀 Key Features & Edge Cases Handled
- **Empty Input**: The function correctly returns an empty list if the input is empty.
- **Single Character Strings**: Handles strings of length 1 correctly as they are their own anagrams.
- **Duplicate Strings**: Identical strings are correctly grouped together in the same list.
- **Empty Strings**: Handles empty strings (e.g., `""`) as valid keys, grouping them together if multiple exist.