from typing import List

## you are given an integer array nums and an integer target.
## you want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
## return the number of different expressions that you can build, which evaluates to target.

class Solution:

    def find_target_sum_ways_recursive(self, nums: List[int], target: int) -> int:
        ## Recursive solution

        ## make a decision for each element in the array
        ## either add it to the sum or subtract it from the sum
        ## return the number of ways to achieve the target

        ## base case is when we have traversed the entire array or we have reached the target 
        ## base case:

        def backtrack(index: int, curr_sum: int) -> int:
            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            return backtrack(index + 1, curr_sum + nums[index]) + \
                   backtrack(index + 1, curr_sum - nums[index])
        
        return backtrack(0, 0)
                    
        


        



if __name__ == "__main__":
    # Test Case 1: Basic case
    solution = Solution()
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    print(f"Test Case 1: nums = {nums1}, target = {target1}")
    print(f"Expected: 5")  # [1+1+1+1-1, 1+1+1-1+1, 1+1-1+1+1, 1-1+1+1+1, -1+1+1+1+1]
    print(f"Output: {solution.find_target_sum_ways(nums1, target1)}\n")

    # Test Case 2: Zero target
    nums2 = [1, 0]
    target2 = 1
    print(f"Test Case 2: nums = {nums2}, target = {target2}")
    print(f"Expected: 2")  # [1+0, 1-0]
    print(f"Output: {solution.find_target_sum_ways(nums2, target2)}\n")

    # Test Case 3: Larger numbers
    nums3 = [2, 3, 4]
    target3 = 5
    print(f"Test Case 3: nums = {nums3}, target = {target3}")
    print(f"Expected: 2")  # [2+3+4, 2-3+4]
    print(f"Output: {solution.find_target_sum_ways(nums3, target3)}\n")

    # Test Case 4: Single element
    nums4 = [5]
    target4 = 5
    print(f"Test Case 4: nums = {nums4}, target = {target4}")
    print(f"Expected: 1")  # [5]
    print(f"Output: {solution.find_target_sum_ways(nums4, target4)}\n")

    # Test Case 5: Impossible target
    nums5 = [1, 1]
    target5 = 4
    print(f"Test Case 5: nums = {nums5}, target = {target5}")
    print(f"Expected: 0")  # No possible combination
    print(f"Output: {solution.find_target_sum_ways(nums5, target5)}")
