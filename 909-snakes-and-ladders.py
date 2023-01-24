
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        flattend_board = reversed(board)
        flattend_board = list(map(lambda x: x[1] if x[0] % 2 == 0 else list(reversed(x[1])), enumerate(flattend_board)))
        flattend_board = [x for sub_list in flattend_board for x in sub_list]

        flattend_board = list(map(lambda x: x - 1 if x != -1 else x, flattend_board))

        goal_index = len(flattend_board) - 1

        current_positions = {0}
        vited_positions = set()
        
        steps = 0
        while current_positions:
            steps += 1

            next_reach = set()
            for current_position in current_positions:
                for reachable in range(current_position + 1, min(current_position+6, goal_index) + 1):
                    target = flattend_board[reachable] if flattend_board[reachable] != -1 else reachable
                    next_reach.add(target)
                vited_positions.add(current_position)
            
            next_reach -= vited_positions
            
            current_positions = next_reach
            if goal_index in current_positions:
                return steps


        return -1




        

ex_board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(Solution().snakesAndLadders(ex_board))