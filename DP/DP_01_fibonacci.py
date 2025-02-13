class Solution:
    def fib_recursive(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)
    

    def fib_dp_memoization(self, n: int) -> int:
        ## Overlapping subproblems are the problems that are solved again and again/ functions that are called multiple times in the recursive tree
        ## Memoization is a technique to store the results of the function calls and return the result from the cache if the function is called again
        ## This is done to avoid the recomputation of the same results
        ## We can use a dict/hashmap to store the results of the function calls
        memo = {
            0:0,
            1:1
        }

        def helper(n):
            if n in memo:
                return memo[n]
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)
    
        ## Time Complexity: O(n)
        ## Space Complexity: O(n)
    
    def fib_dp_tabulation(self, n: int) -> int:
        ## Tabulation is a technique to store the results of the function calls in a table and return the result from the table
        ## We can use a list to store the results of the function calls
        ## We can use a dictionary to store the results of the function calls
        ## It starts as a bottom up approach and builds the solution from the base case usually using loops instead of recursion

        array_dp = [0,1]

        for i in range(2,n+1):
            array_dp.append(array_dp[i-1] + array_dp[i-2])
        return array_dp[n]
    
        ## Time Complexity: O(n)
        ## Space Complexity: O(n)

    def fib_dp_space_optimization(self, n: int) -> int:
        ## Space Optimization is a technique to store the results of the function calls in a single variable instead of using an array
        ## We can use a single variable to store the results of the function calls
        ## We can use a dictionary to store the results of the function calls

        array_dp = [0,1]

        for i in range(2,n+1):
            prev, curr = curr, prev + curr
        return curr
    
        ## Time Complexity: O(n)
        ## Space Complexity: O(1)   
        

        

def main():
    ## Test cases with expected outputs
    test_cases = {
        0: 0,
        1: 1, 
        2: 1,
        5: 5,
        10: 55,
        20: 6765
    }
    solution = Solution()
    
    print("Testing Fibonacci implementations:")
    print("-" * 50)
    
    all_tests_passed = True
    
    for n, expected in test_cases.items():
        print(f"\nTest case n = {n}")
        recursive = solution.fib_recursive(n)
        memoization = solution.fib_dp_memoization(n) 
        tabulation = solution.fib_dp_tabulation(n)
        
        print(f"Recursive: {recursive}")
        print(f"DP Memoization: {memoization}")
        print(f"DP Tabulation: {tabulation}")
        
        # Verify results
        if recursive != expected or memoization != expected or tabulation != expected:
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




        
            


