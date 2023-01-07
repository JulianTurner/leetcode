class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        def get_next_index(base_list: list, current_index: int) -> int:
            if current_index == len(base_list) - 1:
                return 0
            else:
                return current_index + 1
                
        ring_len = len(gas)
        end_index = 0
        current_tank = 0
        
        for start_index in range(ring_len):
            while current_tank + gas[end_index] >= cost[end_index]:
                if get_next_index(gas, end_index) == start_index:
                    return start_index
                current_tank += gas[end_index] - cost[end_index]
                end_index = get_next_index(gas, end_index)
            
            # when start index is end index move end index
            if start_index == end_index:
                end_index = get_next_index(gas, end_index)
                current_tank = 0

            else:
                current_tank -= gas[start_index] - cost[start_index]

        return -1



sol = Solution()
ex_1 = ([1,2,3,4,5], [3,4,5,1,2], 3) # expected 3
ex_2 = ([2,3,4], [3,4,3], -1) # expected -1
ex_3 = ([2], [2], 0) # expected 0
ex_4 = ([5,1,2,3,4], [4,4,1,5,1], 4) # expected 4

examples = [ex_1, ex_2, ex_3, ex_4]
for (gas_ex, cost_ex, expected_ex) in examples:
    result = sol.canCompleteCircuit(gas_ex, cost_ex)
    assert expected_ex == result,\
        f"expected {expected_ex} but got {result} for input gas={gas_ex} cost_ex={cost_ex}"

print('All tests passsed')
