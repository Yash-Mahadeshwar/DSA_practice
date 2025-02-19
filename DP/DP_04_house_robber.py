from typing import List

## You are a professional robber planning to rob houses along a street. 
## Each house has a certain amount of money stashed, nums[i].
## You cannot rob adjacent houses (houses directly next to each other).
## Return the maximum amount of money you can rob.


class Solution:

    def rob_recursive(self, nums: List[int]) -> int:
        ## Recursive solution (top-down)
        ## At each index i, we have two choices:
        ## 1. Rob current house (nums[i]) and skip next house
        ## 2. Skip current house and move to next house
        ## Return maximum amount possible
        
        if not nums:
            return 0
            
        n = len(nums)

        def helper(i):
            # Base cases
            if i == 0:
                return nums[0]  # Only one house to rob
            if i == 1:
                return max(nums[0], nums[1])  # Take max of first two houses
            
            # For each house, choose maximum of:
            # 1. Rob current house + money from i-2 houses
            # 2. Skip current house and take money from i-1 houses
            return max(nums[i] + helper(i-2), helper(i-1))
        
        return helper(n-1)
    
        ## Time Complexity: O(2^n) - each call branches into 2 recursive calls
        ## Space Complexity: O(n) - recursion stack depth
    
    def rob_memo(self, nums: List[int]) -> int:
        ## Memoization solution (top-down DP)
        ## Cache results to avoid recalculating same subproblems
        
        if not nums:
            return 0
            
        memo = {}  # Cache for storing results
        n = len(nums)

        def helper(i):
            # Return cached result if available
            if i in memo:
                return memo[i]
                
            # Base cases
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
                
            # Calculate and cache result for index i
            memo[i] = max(nums[i] + helper(i-2), helper(i-1))
            return memo[i]
        
        return helper(n-1)
            
        ## Time Complexity: O(n) - each subproblem solved once
        ## Space Complexity: O(n) - memoization cache
        
    def rob_tabulation(self, nums: List[int]) -> int:
        ## Tabulation solution (bottom-up DP)
        ## Build solution iteratively using array
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        # dp[i] represents maximum money after considering houses 0 to i
        dp = [0] * len(nums)
        dp[0] = nums[0]  # Max money from first house
        dp[1] = max(nums[0], nums[1])  # Max money from first two houses
        
        # Fill dp table iteratively
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1],  # Skip current house
                       dp[i-2] + nums[i])  # Rob current house + money from i-2 houses
                       
        return dp[-1]  # Return maximum money possible
    
        ## Time Complexity: O(n) - single pass through array
        ## Space Complexity: O(n) - dp array

    def rob_tabulation_space_optimized(self, nums: List[int]) -> int:
        ## Space optimized solution
        ## Instead of keeping entire dp array, just keep last two values
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        # Initialize with first two houses
        rob1 = nums[0]  # Max money if we had only first house
        rob2 = max(nums[0], nums[1])  # Max money from first two houses
        
        # For each house starting from third
        for i in range(2, len(nums)):
            # Current max is max of:
            # 1. Rob current house + money from i-2 houses (rob1)
            # 2. Skip current house and keep money from i-1 houses (rob2)
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2  # Update for next iteration
            rob2 = temp
            
        return rob2
    
        ## Time Complexity: O(n) - single pass through array
        ## Space Complexity: O(1) - only two variables
        
        ## Note: This is the most efficient solution as it:
        ## 1. Uses constant extra space
        ## 2. Makes single pass through array
        ## 3. Has simple, easy to understand logic

def main():
    ## Test cases with expected outputs
    test_cases = {
        'basic': {
            'nums': [1, 2, 3, 1],
            'expected': 4,  # Rob house 1 (money = 1) and then rob house 3 (money = 3)
        },
        'adjacent_high': {
            'nums': [2, 7, 9, 3, 1],
            'expected': 12,  # Rob house 1 (money = 2), house 3 (money = 9), house 5 (money = 1)
        },
        'single_house': {
            'nums': [5],
            'expected': 5,  # Only one house to rob
        },
        'two_houses': {
            'nums': [1, 2],
            'expected': 2,  # Rob the second house
        },
        'three_houses': {
            'nums': [4, 1, 2],
            'expected': 6,  # Rob first house only
        },
        'all_same': {
            'nums': [1, 1, 1, 1],
            'expected': 2,  # Rob any non-adjacent pair
        },
        'empty': {
            'nums': [],
            'expected': 0,  # No houses to rob
        },
        'large_input': {
            'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'expected': 30,  # Rob every other house
        }
    }
    
    solution = Solution()
    all_tests_passed = True
    
    print("Testing House Robber implementations:")
    print("-" * 50)
    
    for test_name, test_data in test_cases.items():
        print(f"\nTest Case: {test_name}")
        nums = test_data['nums']
        expected = test_data['expected']
        
        # Test all implementations
        recursive = solution.rob_recursive(nums)
        memoization = solution.rob_memo(nums)
        tabulation = solution.rob_tabulation(nums)
        
        print(f"Input: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Recursive: {recursive}")
        print(f"Memoization: {memoization}")
        print(f"Tabulation: {tabulation}")
        
        # Verify results
        if any(result != expected for result in [recursive, memoization, tabulation]):
            print(f"❌ Test failed!")
            all_tests_passed = False
        else:
            print(f"✅ Test passed! All implementations returned correct value: {expected}")
        print("-" * 30)
    
    if all_tests_passed:
        print("\nAll test cases passed successfully! 🎉")
    else:
        print("\nSome test cases failed! ❌")

if __name__ == "__main__":
    main()










