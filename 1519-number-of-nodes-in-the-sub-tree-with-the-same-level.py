from collections import defaultdict
from pprint import pprint

class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        neighbours = defaultdict(lambda: set())
        for vertex_a, vertex_b in edges:
            neighbours[vertex_a].add(vertex_b)
            neighbours[vertex_b].add(vertex_a)
        pprint(neighbours)
        
        result = [0 for _ in range(n)]

        def walk_tree(current_vertex: int, prev_vertex: int) -> dict[str, int]:
            count = {labels[current_vertex]:1}

            # down
            for child in neighbours[current_vertex]:
                if child != prev_vertex:
                    child_result = walk_tree(child, current_vertex)
                    for child_label, child_value in child_result.items():
                        if child_label in count:
                            count[child_label] = count[child_label] + child_value
                        else:
                            count[child_label] = child_value
                            
            # back up
            result[current_vertex] = count[labels[current_vertex]]

            return count
        
        walk_tree(0, None)


        return result

ex_n = 7
ex_edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
ex_labels = "abaedcd"
print(Solution().countSubTrees(ex_n, ex_edges,ex_labels)) #[2,1,1,1,1,1,1]