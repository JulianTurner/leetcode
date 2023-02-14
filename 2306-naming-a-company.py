from collections import defaultdict
from itertools import combinations

class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        ideas_dict = defaultdict(lambda: set())

        for idea in ideas:
            ideas_dict[idea[0]].add(idea[1:])
        
        ideas_list = list(ideas_dict.values())

        result = 0

        for first_set, second_set in combinations(ideas_list, 2):
                first_unique = first_set - second_set
                second_unique = second_set - first_set
                result += (len(first_unique) * len (second_unique))


        return result * 2

ex_ideas = ["coffee","donuts","time","toffee"]
print(Solution().distinctNames(ex_ideas)) # 6