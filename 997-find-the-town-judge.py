class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        trusts_count = [0] * (n+1)
        trusted_count = [0] * (n+1)

        for truster, trustee in trust:
            trusts_count[truster] += 1
            trusted_count[trustee] += 1

        
        
        for label, (trusts_other, trusted_by) in enumerate(zip(trusts_count, trusted_count)):
            if trusts_other == 0 and trusted_by == n-1:
                return  label
        
        return -1 

ex_n = 3
ex_trust = [[1,3],[2,3],[3,1]]
print(Solution().findJudge(ex_n, ex_trust))