## Question: You are climbing a staircase. It takes n steps to reach the top.
## Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:

    def climbing_stairs_recursive(self, n: int) -> int:
        ## Recursive solution
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return  self.climbing_stairs_recursive(n-1) +  self.climbing_stairs_recursive(n-2)
        
        ## Time Complexity: O(2^n)
        ## Space Complexity: O(n)
        
    def climbing_stairs_memoization(self, n: int) -> int:
        ## Memoization solution
        memo = {
            1: 1,
            2: 2
        }

        def helper(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = helper(n-1) + helper(n-2)
                return memo[n]
        return helper(n)
    
        ## Time Complexity: O(n)
        ## Space Complexity: O(n)

    def climbing_stairs_tabulation(self, n: int) -> int:
        ## Tabulation solution
        dp = [None]*(n+1)

        dp[0] = 1
        dp[1] = 2
        
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]
    
        ## Time Complexity: O(n)
        ## Space Complexity: O(n)

    def climbing_stairs_optimized(self, n: int) -> int:
        ## Space Optimization solution
        if n==1:
            return 1
        if n==2:
            return 2
        prev, curr = 1, 2

        for i in range(2,n):
            prev, curr = curr, prev + curr

        return curr
    
        ## Time Complexity: O(n)
        ## Space Complexity: O(1)
        
    



        

 

def main():
    ## Test cases with expected outputs
    test_cases = {
        1: 1,    # 1 way: [1]
        2: 2,    # 2 ways: [1,1], [2]
        3: 3,    # 3 ways: [1,1,1], [1,2], [2,1]
        4: 5,    # 5 ways: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]
        5: 8,    # 8 ways
        6: 13    # 13 ways
    }
    
    solution = Solution()
    print("Testing Climbing Stairs implementations:")
    print("-" * 50)
    
    all_tests_passed = True
    
    for n, expected in test_cases.items():
        print(f"\nTest case n = {n}")
        recursive = solution.climbing_stairs_recursive(n)
        memoization = solution.climbing_stairs_memoization(n)
        tabulation = solution.climbing_stairs_tabulation(n)
        optimized = solution.climbing_stairs_optimized(n)
        
        print(f"Recursive: {recursive}")
        print(f"DP Memoization: {memoization}")
        print(f"DP Tabulation: {tabulation}")
        print(f"Space Optimized: {optimized}")
        
        # Verify results
        if any(result != expected for result in [recursive, memoization, tabulation, optimized]):
            print(f"❌ Test failed! Expected {expected}")
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
