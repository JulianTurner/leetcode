from functools import cache

class Solution:
    def is_palindrome(self, s: str) -> bool:
        for i, c in enumerate(s):
            if i > len(s)/2:
                break
            if c != s[-(i+1)]:
                return False
        return True
        
    def partition(self, s: str) -> list[list[str]]:

        @cache
        def get_palindrome(start_index: int) -> list[str]:
            curr_str = ""
            palindromes_here = []
            for i in range(start_index, len(s)):
                curr_str += s[i]
                if self.is_palindrome(curr_str):
                    palindromes_here.append(curr_str)

            return palindromes_here

        
        solutions = []
        def string_walker(solution_so_far: list[str], current_poition: int):
            if current_poition == len(s) - 1:
                solutions.append(solution_so_far + [s[current_poition]])
                return
            
            palindromes_from_here = get_palindrome(current_poition)

            for palindrome in palindromes_from_here:
                next_index = current_poition + len(palindrome)
                if next_index > len(s) - 1:
                    solutions.append(solution_so_far + [palindrome])
                else:
                    string_walker(solution_so_far + [palindrome], next_index)

        string_walker([], 0)
        return solutions

ex_s = "bb"
print(Solution().partition(ex_s)) # [["b","b"],["bb"]]