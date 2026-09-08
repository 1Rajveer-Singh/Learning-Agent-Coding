from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    """
    Determines if string 't' is an anagram of string 's'.
    
    An anagram is a word or phrase formed by rearranging the letters 
    of a different word or phrase, typically using all the original 
    letters exactly once.
    """
    # If lengths differ, they cannot be anagrams
    if len(s) != len(t):
        return False
    
    # Use a frequency map (hash map) to count occurrences of each character
    # Time Complexity: O(N), Space Complexity: O(K) where K is alphabet size
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Compare the frequency maps
    return count_s == count_t