from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in the array which gives the sum of zero.
    Uses the sorting + two-pointer approach for optimal performance.
    """
    nums.sort()
    results = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate values for the first element to ensure unique triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Optimization: If the smallest number is > 0, sum can never be 0
        if nums[i] > 0:
            break
            
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # Found a triplet
                results.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
                
    return results