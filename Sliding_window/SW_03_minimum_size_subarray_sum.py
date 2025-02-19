from typing import List

## Given an array of positive integers nums and a positive integer target,
## return the minimal length of a subarray whose sum is greater than or equal to target.
## Return 0 if no such subarray exists.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ## Sliding Window approach:
        ## - Use two pointers (l,r) to maintain a window
        ## - Expand window by adding numbers until sum >= target
        ## - Then shrink window from left while sum still >= target
        
        l = 0  # Left pointer of window
        total = 0  # Current sum of elements in window
        min_len = float('inf')  # Track minimum length found (initialize to infinity)
        
        # Right pointer expands window
        for r in range(len(nums)):
            total += nums[r]  # Add current number to window sum
            
            # While window sum is valid, try to minimize window size
            while total >= target:
                min_len = min(min_len, r - l + 1)  # Update minimum length if smaller
                total -= nums[l]  # Remove leftmost number from sum
                l += 1  # Shrink window from left
                
        return min_len if min_len != float('inf') else 0  # Return 0 if no valid window found
    
        ## Time Complexity: O(n)
        ## - Each element is added and removed at most once
        ## - Both pointers traverse the array once
        
        ## Space Complexity: O(1)
        ## - Only using a few variables regardless of input size
        
        ## Example:
        ## nums = [2,3,1,2,4,3], target = 7
        ## [2] -> sum=2
        ## [2,3] -> sum=5
        ## [2,3,1] -> sum=6
        ## [2,3,1,2] -> sum=8 (valid) -> try shrinking: [3,1,2] -> sum=6
        ## [3,1,2,4] -> sum=10 (valid) -> try shrinking: [1,2,4] -> sum=7 (valid) -> [2,4] -> sum=6
        ## [2,4,3] -> sum=9 (valid) -> try shrinking: [4,3] -> sum=7 (valid)
        ## Final answer: 2 (subarray [4,3])


        