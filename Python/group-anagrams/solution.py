from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups an array of strings into anagrams using a hash map.
    
    Args:
        strs: A list of strings to be grouped.
        
    Returns:
        A list of lists, where each inner list contains strings that are anagrams.
    """
    # Dictionary to store the mapping of sorted string key to list of anagrams
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Sort the string to create a canonical representation (key)
        # Anagrams will result in the same sorted string
        sorted_key = "".join(sorted(s))
        
        # Append the original string to the list corresponding to the sorted key
        anagram_map[sorted_key].append(s)
        
    # Return all grouped lists
    return list(anagram_map.values())