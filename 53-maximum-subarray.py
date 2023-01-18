from math import inf


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_so_far = -inf
        max_ending_here = 0

        for el in nums:
            max_ending_here += el
            max_so_far = max(max_so_far, max_ending_here)
            max_ending_here = max(max_ending_here, 0)
        
        return max_so_far

ex_nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(ex_nums))