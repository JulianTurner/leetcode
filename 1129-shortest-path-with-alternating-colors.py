from collections import defaultdict
from math import inf

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        red_network = defaultdict(lambda: [])
        blue_network = defaultdict(lambda: [])


        for (src, dest) in redEdges:
            red_network[src].append(dest)
        
        for (src, dest) in blueEdges:
            blue_network[src].append(dest)

        result_both_colors = [[inf, inf] for _ in range(n)] # [red_reach_in, blue_reached_in]
        result_both_colors[0] = [0, 0]

        def network_walker(current_step: int, red_edges_from: set[int], blue_edges_from: set[int]):
            reached_with_red_edges = set()

            for src in red_edges_from:
                for dest in red_network[src]:
                    if current_step < result_both_colors[dest][0]:
                        result_both_colors[dest][0] = current_step
                        reached_with_red_edges.add(dest)

            reached_with_blue_edges = set()

            for src in blue_edges_from:
                for dest in blue_network[src]:
                    if current_step < result_both_colors[dest][1]:
                        result_both_colors[dest][1] = current_step
                        reached_with_blue_edges.add(dest)

            if (not reached_with_red_edges) and (not reached_with_blue_edges):
                return
            
            network_walker(current_step + 1, reached_with_blue_edges, reached_with_red_edges)

        network_walker(1, {0}, {0})

        def res_transformer(result_red_blue: list[int]):
            if (result_red_blue[0] == inf) and (result_red_blue[1] == inf):
                return -1
            return min(result_red_blue[0], result_red_blue[1])

        return list(map(res_transformer, result_both_colors))


ex_n = 3 
ex_redEdges = [[0,1]] 
ex_blueEdges = [[1,2]]
print(Solution().shortestAlternatingPaths(ex_n, ex_redEdges, ex_blueEdges)) # [0,1,2]