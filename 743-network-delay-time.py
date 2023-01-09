from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # defaultdict: current_node -> [[targetA, inTime], [targetB, inTime], ...]
        node_dict = defaultdict(lambda: [])
        for (src, dest, travel_time) in times:
            node_dict[src].append([dest, travel_time])
        print(node_dict)

        shortest_paths = {k: 0}

        visited_nodes = set()
    
        while len(visited_nodes) != len(shortest_paths):
            #find next reachable node with shortest parth so far
            next_node = min(set(shortest_paths.keys()).difference(visited_nodes), key=lambda x: shortest_paths[x])

            if next_node in node_dict:
                print(next_node)
                for connection in node_dict[next_node]:
                    reached_in = shortest_paths[next_node] + connection[1]
                    if (connection[0] not in shortest_paths)  or (shortest_paths[connection[0]] > reached_in):
                        shortest_paths[connection[0]] = reached_in
                        
            visited_nodes.add(next_node)
        

        if(len(shortest_paths) != n):
            return -1

        print(shortest_paths)
        return max(shortest_paths.values())


sol = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 2
k = 1
print(sol.networkDelayTime(times, n , k))
