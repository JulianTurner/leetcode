from pprint import pprint

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        chars_to_set = {}
        for a, b in zip(s1, s2):
            a_known = a in chars_to_set
            b_known = b in chars_to_set
            
            if a_known and b_known: # both known
                for char_from_b in chars_to_set[b]:
                    chars_to_set[a].add(char_from_b)
                    chars_to_set[char_from_b] = chars_to_set[a]
            elif a_known: # a known - b unkown
                chars_to_set[a].add(b)
                chars_to_set[b] = chars_to_set[a]
            elif b_known: # a unknown - b known
                chars_to_set[b].add(a)
                chars_to_set[a] = chars_to_set[b]
            else: # create new set
                new_set = {a,b}
                chars_to_set[a] = new_set
                chars_to_set[b] = new_set

        pprint(chars_to_set)

        for k, v in chars_to_set.items():
            print(f'{k}: {id(v)}')

        find_smallest_cache = {}
        def find_smallest(some_set):
            if id(some_set) in find_smallest_cache:
                return find_smallest_cache[id(some_set)]
            find_smallest_cache[id(some_set)] = min(some_set)
            return find_smallest_cache[id(some_set)]
        
        final_mapping = {k: find_smallest(v) for k, v in  chars_to_set.items()}

        pprint(final_mapping)

        return "".join(map(lambda x: final_mapping[x] if x in final_mapping else x, baseStr))


ex_s1 = "leetcode"
ex_s2 = "programs"
ex_baseStr = "sourcecode"

print(Solution().smallestEquivalentString(ex_s1, ex_s2, ex_baseStr))