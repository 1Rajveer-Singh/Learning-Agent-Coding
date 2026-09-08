from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Finds the indices of two numbers in the list that add up to the target.
    
    Uses a hash map (dictionary) to store the complement of each number 
    encountered so far, allowing for O(1) average time complexity lookups.
    """
    # Dictionary to store {value: index}
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If the complement exists in the map, we found the pair
        if complement in seen:
            return [seen[complement], i]
        
        # Otherwise, store the current number and its index
        seen[num] = i
        
    # Return an empty list if no solution is found (though problem constraints usually guarantee one)
    return []