
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        word_arr = s.split(' ')
        pattern_arr = list(pattern)
        if len(word_arr) != len(pattern_arr):
            return False

        vals1 = dict(zip(word_arr, pattern_arr))
        vals2 = dict(zip(pattern_arr, word_arr))

        for i in range(len(word_arr)):
            print(word_arr[i], pattern_arr[i])
            if (word_arr[i], pattern_arr[i]) not in vals1.items():
                return False
            if (pattern_arr[i], word_arr[i]) not in vals2.items():
                return False

        return True


pattern = "abba"
s = "dog cat cat fish"
sol = Solution()
print(sol.wordPattern(pattern, s))
