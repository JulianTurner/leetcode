

class Solution:
    def __init__(self) -> None:
        self.trib_cache = {0:0,1:1,2:1}
        pass

    def tribonacci(self, n: int) -> int:
        if n in self.trib_cache:
            return self.trib_cache[n]
        
        result = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.trib_cache[n] = result
        
        return result

ex_n = 4
print(Solution().tribonacci(ex_n)) # 4