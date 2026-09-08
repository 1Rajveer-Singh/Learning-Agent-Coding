def isPalindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, considering only alphanumeric 
    characters and ignoring cases.
    """
    # Initialize two pointers at the start and end of the string
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer forward if current char is not alphanumeric
        if not s[left].isalnum():
            left += 1
        # Move right pointer backward if current char is not alphanumeric
        elif not s[right].isalnum():
            right -= 1
        # Compare characters; if they don't match, it's not a palindrome
        else:
            if s[left].lower() != s[right].lower():
                return False
            # Move both pointers inward after a successful match
            left += 1
            right -= 1
            
    return True