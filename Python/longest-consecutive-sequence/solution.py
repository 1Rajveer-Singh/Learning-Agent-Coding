def longest_consecutive(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence.
    
    Args:
        nums: A list of integers.
        
    Returns:
        The length of the longest consecutive sequence.
    """
    # Convert list to a set for O(1) average time complexity lookups
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if 'num' is the start of a sequence.
        # If 'num - 1' exists, 'num' is not the start.
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Incrementally check for the next numbers in the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the global maximum
            longest_streak = max(longest_streak, current_streak)

    return longest_streak