class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        decresing_numbers = set()

        num_stack = []
        def number_runner(remaining_nums: list[int]):

            for i, num in enumerate(remaining_nums):
                if num_stack and num < num_stack[-1]:
                    continue
                num_stack.append(num)
                if len(num_stack) >= 2:
                    decresing_numbers.add(tuple(num_stack))
                number_runner(remaining_nums[i+1:])
                num_stack.pop()
            
        number_runner(nums)

        return list(map(lambda x: list(x), decresing_numbers))

ex_nums = [4,6,7,7]
print(Solution().findSubsequences(ex_nums)) # [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]