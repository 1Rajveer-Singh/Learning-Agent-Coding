from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Calculates the product of all elements in the array except the element at the current index.
    
    Logic:
    1. Use a result array to store the prefix products (product of all elements to the left).
    2. Iterate backwards to calculate the suffix products (product of all elements to the right)
       and multiply them into the result array on the fly.
    """
    n = len(nums)
    if n == 0:
        return []
    
    # Initialize result array with 1s
    res = [1] * n
    
    # Step 1: Calculate prefix products
    # res[i] will contain the product of all elements to the left of nums[i]
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
        
    # Step 2: Calculate suffix products and multiply with existing prefix products
    # suffix keeps track of the product of all elements to the right of nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
        
    return res