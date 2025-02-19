## Longest Substring Without Repeating Characters
## Given a string s, find the length of the longest substring without repeating characters.
## Example: "abcabcbb" -> 3 ("abc")

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Sliding Window approach:
        ## - Use two pointers (l,r) to maintain a window of unique characters
        ## - Use a set to track unique characters in current window
        ## - When we find a duplicate, shrink window from left until duplicate is removed
        
        # Handle empty string
        if len(s) == 0:
            return 0
            
        l = 0  # Left pointer of window
        max_len = 0  # Track maximum length found
        set_unique = set()  # Track unique characters in current window
        
        # Right pointer expands window
        for r in range(len(s)):
            # If current character is in set, shrink window from left
            while s[r] in set_unique:
                set_unique.remove(s[l])  # Remove leftmost character
                l += 1  # Shrink window
                
            set_unique.add(s[r])  # Add current character to set
            max_len = max(max_len, r - l + 1)  # Update max length if needed
            
        return max_len
    
        ## Time Complexity: O(n) 
        ## - Each character is added and removed at most once
        ## - Both pointers traverse the string once
        
        ## Space Complexity: O(min(m,n)) where:
        ## - n is length of string
        ## - m is size of character set (e.g., 26 for lowercase letters)
        ## - Set will never be larger than unique characters possible
            
            
        