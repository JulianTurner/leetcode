class Solution():
    def climbStairs(self, n: int) -> int:
        # check if n is 1 or 2
        if (n == 1):
            return 1
        if (n == 2):
            return 2 
        if (n > 2): 
            first = 1
            second = 2 
            for i in range(2,n):
                third = first + second
                first = second
                second = third

            return third
# run the code
n = 38 
solution = Solution()
print(solution.climbStairs(n))
