## Problem: A robot is located at the top-left corner of a m x n grid
## The robot can only move either down or right at any point in time
## The robot is trying to reach the bottom-right corner of the grid
## How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ## Recursive solution (top-down)
        ## At each cell (i,j), robot can:
        ## 1. Move right to (i,j+1)
        ## 2. Move down to (i+1,j)
        
        def helper(i, j):
            # Base case: when we reach first row or first column
            # There's only 1 way to reach any cell in first row/column
            def helper(i, j):
                if i == j == 0:
                    return 1
                if i < 0 or j < 0 or i == m or j == n:
                    return 0
                else:
                    return helper(i-1, j) + helper(i, j-1)
            
            return helper(m-1, n-1)
                

                
            # For each cell, paths = paths from above + paths from left
    
        
        return helper(m-1, n-1)
        
        ## Time Complexity: O(2^(m*8n)) - each call branches into 2 recursive calls
        ## Space Complexity: O(m+n) - maximum recursion depth
        
        ## Note: This recursive solution will be very slow for large grids
        ## Better to use DP with memoization or tabulation
    def uniquePaths_memo(self, m: int, n: int) -> int:
        memo  = {}        
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == 0 or j == 0:
                return 1
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                memo[(i, j)] = helper(i-1, j) + helper(i, j-1)
                return memo[(i, j)]
        
        return helper(m-1, n-1)
    
    
    def uniquePaths_tabulation(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            dp.append([0] * n)
        
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                val = 0
                if  i > 0:
                    val += dp[i-1][j]
                if j > 0:
                    val += dp[i][j-1]
                dp[i][j] = val
        return dp[m-1][n-1]
    
    def uniquePaths_space_optimized(self, m: int, n: int) -> int:
        prev = [1] * n
        for i in range(1, m):
            curr = [1] * n
            for j in range(1, n):
                curr[j] = curr[j-1] + prev[j]
                
                    

def main():
    ## Test cases with expected outputs
    test_cases = {
        'small_grid': {
            'm': 2,
            'n': 2,
            'expected': 2,  # Right->Down, Down->Right
        },
        'medium_grid': {
            'm': 3,
            'n': 3,
            'expected': 6,  # RR->D, R->D->R, R->DR, D->R->R, DR->R, DD->R
        },
        'rectangular': {
            'm': 3,
            'n': 7,
            'expected': 28,
        },
        'single_row': {
            'm': 1,
            'n': 5,
            'expected': 1,  # Only one way - all right moves
        },
        'single_column': {
            'm': 5,
            'n': 1,
            'expected': 1,  # Only one way - all down moves
        },
        'large_grid': {
            'm': 10,
            'n': 10,
            'expected': 48620,  # Test performance of different approaches
        }
    }
    
    solution = Solution()
    all_tests_passed = True
    
    print("Testing Unique Paths implementations:")
    print("-" * 50)
    
    for test_name, test_data in test_cases.items():
        print(f"\nTest Case: {test_name}")
        m, n = test_data['m'], test_data['n']
        expected = test_data['expected']
        
        # Test all implementations
        recursive = solution.uniquePaths(m, n)
        memoization = solution.uniquePaths_memo(m, n)
        tabulation = solution.uniquePaths_tabulation(m, n)
        optimized = solution.uniquePaths_space_optimized(m, n)
        
        print(f"Input: m = {m}, n = {n}")
        print(f"Expected: {expected}")
        print(f"Recursive: {recursive}")
        print(f"Memoization: {memoization}")
        print(f"Tabulation: {tabulation}")
        print(f"Space Optimized: {optimized}")
        
        # Verify results
        results = [recursive, memoization, tabulation, optimized]
        if any(result != expected for result in results):
            print(f"❌ Test failed!")
            # Show which implementations failed
            if recursive != expected:
                print(f"  Recursive failed: got {recursive}, expected {expected}")
            if memoization != expected:
                print(f"  Memoization failed: got {memoization}, expected {expected}")
            if tabulation != expected:
                print(f"  Tabulation failed: got {tabulation}, expected {expected}")
            if optimized != expected:
                print(f"  Optimized failed: got {optimized}, expected {expected}")
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
        
    
    