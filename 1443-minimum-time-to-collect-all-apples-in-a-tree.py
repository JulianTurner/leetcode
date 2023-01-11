from collections import defaultdict
from pprint import pprint

class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        neighbours = defaultdict(lambda: set())
        for vertex_a, vertex_b in edges:
            neighbours[vertex_a].add(vertex_b)
            neighbours[vertex_b].add(vertex_a)
        pprint(neighbours)
        
        sum_visited_nodes = 0

        def walk_tree(current_vertex: int, prev_vertex: int) -> bool:
            walk_current = hasApple[current_vertex]

            for child in neighbours[current_vertex]:
                if child != prev_vertex:
                    if walk_tree(child, current_vertex):
                        walk_current = True

            if walk_current:
                nonlocal sum_visited_nodes 
                sum_visited_nodes += 1

            return walk_current
        
        walk_tree(0, None)

        if sum_visited_nodes == 0:
            return 0

        return (sum_visited_nodes - 1) * 2


ex_n = 7
ex_edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]

ex_hasApple = [False,False,False,False,False,False,False]
print(Solution().minTime(ex_n, ex_edges, ex_hasApple))
