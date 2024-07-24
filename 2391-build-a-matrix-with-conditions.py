from typing import List


class Solution:

    def topologicalSort(self, k: int, conditions:List[List[int]]):
        indegree = {i: 0 for i in range(1,k+1)}
        
        node_to_other = {}
        for (first, second) in conditions:
            indegree[second] += 1
            node_to_other.setdefault(first, []).append(second)

        print(f'indegree {indegree}')
        print(f'node to others: {node_to_other}')

        result = []
        queue = []

        for (key, value) in indegree.items():
            if value == 0:
                queue.append(key)

        for key in queue:
            indegree.pop(key)

        while queue:
            val = queue.pop()
            result.append(val)
            if val in node_to_other:
                for other in node_to_other[val]:
                    indegree[other] -= 1
                    if indegree[other] == 0:
                        indegree.pop(other)
                        queue.append(other)
        if indegree:
            return None
        return result


    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        sorted_rows =   self.topologicalSort(k, rowConditions)
        print(f'sorted rows {sorted_rows}')
        sorted_columns = self.topologicalSort(k, colConditions)
        print(f'sorted columns {sorted_columns}')

        if sorted_rows is None or sorted_columns is None:
            return []

        result =[[0 for _ in range(k)] for _ in range(k) ]
        sorted_columns_dict = {v:i for (i,v) in enumerate(sorted_columns)}
        for (i,v) in enumerate(sorted_rows):
            result[i][sorted_columns_dict[v]] = v
        print(result)
        return result



k = 3
rowConditions = [[1,2],[2,3],[3,1],[2,3]]
colConditions = [[2,1]]
print(Solution().buildMatrix(k, rowConditions,colConditions )) #[2,1,1,1,1,1,1]