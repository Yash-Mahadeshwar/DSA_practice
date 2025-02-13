from collections import defaultdict
from typing import List

## you are given an integer array nums and an integer target.
## you want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
## return the number of different expressions that you can build, which evaluates to target.

class Solution:

    def find_target_sum_ways_recursive(self, nums: List[int], target: int) -> int:
        ## Recursive solution - Time: O(2^n), Space: O(n)
        ## For each number, we try both + and - operations recursively
        
        def helper(i, curr_sum):
            # Base case: when we've used all numbers
            if i == len(nums):
                return 1 if curr_sum == target else 0
                
            # Try adding current number
            option1 = helper(i+1, curr_sum + nums[i])
            # Try subtracting current number
            option2 = helper(i+1, curr_sum - nums[i])
            
            return option1 + option2
        
        return helper(0, 0)
    

    def find_target_sum_ways_memo(self, nums: List[int], target: int) -> int:
        ## Memoization solution - Time: O(n*sum), Space: O(n*sum)
        ## Cache results to avoid recalculating same states
        
        memo = {}  # Store (index, current_sum) -> number of ways
        
        def helper(i, curr_sum):
            # Return cached result if available
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            # Base case: when we've used all numbers
            if i == len(nums):
                return 1 if curr_sum == target else 0
            
            # Cache and return result for current state
            memo[(i, curr_sum)] = helper(i+1, curr_sum + nums[i]) + helper(i+1, curr_sum - nums[i])
            return memo[(i, curr_sum)]
        
        return helper(0, 0)
    

    def find_target_sum_ways_tabulation_with_table(self, nums: List[int], target: int) -> int:
        ## Tabulation solution - Time: O(n*sum), Space: O(n*sum)
        ## Build solution bottom-up using a 2D table
        
        # dp[i][sum] represents number of ways to achieve sum using first i elements
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        
        # Base case: empty subset can make sum=0 in one way
        dp[0][0] = 1
        
        # Fill dp table
        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                # Add current number
                dp[i + 1][curr_sum + nums[i]] += count
                # Subtract current number
                dp[i + 1][curr_sum - nums[i]] += count
        
        return dp[len(nums)][target]
    

    def find_target_sum_ways_tabulation_with_table_space_optimized(self, nums: List[int], target: int) -> int:
        ## Space optimized tabulation - Time: O(n*sum), Space: O(sum)
        ## Only keep track of current state instead of full table
        
        # Current state: maps sum -> number of ways
        dp = defaultdict(int)
        dp[0] = 1  # Base case
        
        # For each number
        for num in nums:
            next_dp = defaultdict(int)
            # For each current sum and its count
            for curr_sum, count in dp.items():
                # Try both + and - operations
                next_dp[curr_sum + num] += count
                next_dp[curr_sum - num] += count
            dp = next_dp  # Update current state
        
        return dp[target]










            
            



    

        
                    
        

# def find_target_sum_ways_memo(self, nums: List[int], target: int) -> int:

# def find_target_sum_ways_tabulation(self, nums: List[int], target: int) -> int:



def main():
    ## Test cases with expected outputs
    test_cases = {
        'basic': {
            'nums': [1, 1, 1, 1, 1],
            'target': 3,
            'expected': 5,  # [1+1+1+1-1, 1+1+1-1+1, 1+1-1+1+1, 1-1+1+1+1, -1+1+1+1+1]
        },
        'zero_target': {
            'nums': [1, 0],
            'target': 1,
            'expected': 2,  # [1+0, 1-0]
        },
        'larger_nums': {
            'nums': [2, 3, 4],
            'target': 5,
            'expected': 3,  # [2+3+4, 2-3+4]
        },
        'single_element': {
            'nums': [5],
            'target': 5,
            'expected': 1,  # [5]
        },
        'impossible': {
            'nums': [1, 1],
            'target': 4,
            'expected': 0,  # No possible combination
        }
    }
    
    solution = Solution()
    all_tests_passed = True
    
    print("Testing Target Sum implementations:")
    print("-" * 50)
    
    for test_name, test_data in test_cases.items():
        print(f"\nTest Case: {test_name}")
        nums = test_data['nums']
        target = test_data['target']
        expected = test_data['expected']
        
        # Test all implementations
        recursive = solution.find_target_sum_ways_recursive(nums, target)
        # memo = solution.find_target_sum_ways_memo(nums, target)  # Uncomment when implemented
        # tabulation = solution.find_target_sum_ways_tabulation(nums, target)  # Uncomment when implemented
        
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Recursive: {recursive}")
        # print(f"Memoization: {memo}")  # Uncomment when implemented
        # print(f"Tabulation: {tabulation}")  # Uncomment when implemented
        
        # Verify results
        if recursive != expected:  # Add other implementations when ready
            print(f"❌ Test failed!")
            all_tests_passed = False
        else:
            print(f"✅ Test passed!")
        print("-" * 30)
    
    if all_tests_passed:
        print("\nAll test cases passed successfully! 🎉")
    else:
        print("\nSome test cases failed! ❌")

if __name__ == "__main__":
    main()
