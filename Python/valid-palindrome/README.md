# Valid Palindrome

## 💡 Overview & Approach
The problem is solved using the **Two-Pointer Technique**, which is highly efficient for string manipulation tasks involving symmetry. We initialize two pointers: one at the beginning (`left`) and one at the end (`right`) of the string. 

The algorithm iterates inward, skipping any non-alphanumeric characters by incrementing the `left` pointer or decrementing the `right` pointer. Once both pointers land on alphanumeric characters, we compare them in a case-insensitive manner. If at any point the characters do not match, we immediately return `False`. If the pointers meet or cross without finding a mismatch, the string is confirmed to be a palindrome.

## 📊 Complexity Analysis
- **Time Complexity**: **O(N)**, where N is the length of the string. We traverse the string at most once using the two pointers.
- **Space Complexity**: **O(1)**. We perform the check in-place without allocating extra data structures (like a filtered string or a reversed copy).

## 🏢 Top Companies Asking This Problem
- Meta (Facebook)
- Google
- Amazon
- Microsoft
- Apple
- Uber

## 🚀 Key Features & Edge Cases Handled
- **Case Insensitivity**: Uses `.lower()` to ensure 'A' and 'a' are treated as identical.
- **Non-Alphanumeric Filtering**: Uses `.isalnum()` to ignore spaces, punctuation, and symbols, satisfying the problem constraints.
- **Empty Strings/Single Characters**: An empty string or a single-character string naturally returns `True`, as the loop condition `left < right` is never met or the pointers immediately cross.
- **All Non-Alphanumeric Strings**: Strings containing only symbols (e.g., "!!!") are correctly identified as palindromes (vacuously true).