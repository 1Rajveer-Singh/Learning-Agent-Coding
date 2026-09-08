from typing import List

def maxArea(height: List[int]) -> int:
    """
    Calculates the maximum area of water a container can store.
    Uses the two-pointer approach to achieve linear time complexity.
    """
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Calculate the width between the two pointers
        width = right - left
        
        # The height of the container is limited by the shorter line
        h_left = height[left]
        h_right = height[right]
        current_height = min(h_left, h_right)
        
        # Calculate area and update max_water if current is larger
        max_water = max(max_water, width * current_height)
        
        # Move the pointer pointing to the shorter line inward.
        # Moving the taller line would only decrease the width without 
        # the possibility of increasing the height.
        if h_left < h_right:
            left += 1
        else:
            right -= 1
            
    return max_water