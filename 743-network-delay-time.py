from collections import defaultdict
import math

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # defaultdict: current_node -> [[targetA, inTime], [targetB, inTime], ...]
        node_dict = defaultdict(lambda: [])
        for (src, dest, travel_time) in times:
            node_dict[src].append([dest, travel_time])

        if n == k:
            for con in node_dict[n]:
                if(con[0] == k):
                    return con[1]

            return -1
        
        
        unvisited_nodes = set(node_dict.keys())
        # visited_nodes = []
        shortest_paths = {}
        for vertex in unvisited_nodes:
            shortest_paths[vertex] = [math.inf, None]

        shortest_paths[k] = [0, None]

        while len(unvisited_nodes) > 0:
            smallest_unvisited_dist = math.inf
            smallest_unvisited_vertex = None
            
            for unvisted_node in unvisited_nodes:
                if shortest_paths[unvisted_node][0] <= smallest_unvisited_dist:
                    smallest_unvisited_dist = shortest_paths[unvisted_node][0]
                    smallest_unvisited_vertex = unvisted_node

            for connection in node_dict[smallest_unvisited_vertex]:
                reached_in = smallest_unvisited_dist + connection[1]
                if (connection[0] not in shortest_paths) or (reached_in < shortest_paths[connection[0]][0]):
                    shortest_paths[connection[0]] = [reached_in, smallest_unvisited_vertex]

            unvisited_nodes.remove(smallest_unvisited_vertex)
        
        if n in shortest_paths:
            return shortest_paths[n][0]
            
        return -1



sol = Solution()
times = [[1,2,1],[2,1,3]]
n = 2
k = 2
print(sol.networkDelayTime(times, n , k))
