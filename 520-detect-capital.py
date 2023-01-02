import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        pattern = r'^[A-Z][a-z]*$|^[a-z]*$|^[A-Z]*$'
        result = re.findall(pattern, word)
        if len(result) > 0:
            return True
        return False
        

sol = Solution()
print(sol.detectCapitalUse("USA"))