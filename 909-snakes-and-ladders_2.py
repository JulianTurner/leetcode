from math import inf


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        flattend_board = reversed(board)
        flattend_board = list(map(lambda x: x[1] if x[0] % 2 == 0 else list(reversed(x[1])), enumerate(flattend_board)))
        flattend_board = [x for sub_list in flattend_board for x in sub_list]

        flattend_board = list(map(lambda x: x - 1 if x != -1 else x, flattend_board))

        goal_index = len(flattend_board) - 1

        unvisited_nodes = set(range(goal_index+1))
        visited_nodes = set()

        shortest_path = {x: inf for x in unvisited_nodes}
        shortest_path[0] = 0

        while unvisited_nodes:
            smallest_unvisited = -1
            smallest_unvisited_in = inf
            for unvisited_node in unvisited_nodes:
                if smallest_unvisited_in >= shortest_path[unvisited_node]:
                    smallest_unvisited = unvisited_node
                    smallest_unvisited_in = shortest_path[unvisited_node]

            if smallest_unvisited_in == inf:
                break

            next_step_to = smallest_unvisited_in + 1
            for target in range(smallest_unvisited + 1, min(smallest_unvisited + 6, goal_index) + 1):
                true_target = flattend_board[target] if flattend_board[target] != -1 else target
                shortest_path[true_target] = min(shortest_path[true_target], next_step_to)

            unvisited_nodes.remove(smallest_unvisited)
            visited_nodes.add(smallest_unvisited)
        
        if shortest_path[goal_index] == inf:
            return -1
        
        return shortest_path[goal_index]
                
        

ex_board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(Solution().snakesAndLadders(ex_board))