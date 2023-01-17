class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = s.count('0')
        min_flips = flips
        for c in s:
            if c == '1':
                flips += 1
            else:
                flips -= 1
            min_flips = min(min_flips, flips)
        return min_flips


ex_s = "00110"
print(Solution().minFlipsMonoIncr(ex_s))

