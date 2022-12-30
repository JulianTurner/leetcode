from functools import cache

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        last_nr = len(graph) - 1


        # for current node get the next nodes
        @cache
        def get_next_node(current: int) -> list[list[int]]:
            if current == last_nr:
                return [[last_nr]]

            paths = []
            for node in graph[current]: # iterate through children
                for child_path in get_next_node(node): # iterate through solutions of child
                    current_child_path = list(child_path)
                    current_child_path.insert(0,current)
                    paths.append(current_child_path)

            return paths
        return get_next_node(0)

examle_graph = [[4,3,1],[3,2,4],[3],[4],[]]
sol = Solution()
print(sol.allPathsSourceTarget(examle_graph))
