class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        min_arrow_shots = 1
        points.sort(key=lambda x: x[1])
        shoot_next = points[0][1]
        for ballon in points:
            if ballon[0] > shoot_next:
                shoot_next = ballon[1]
                min_arrow_shots += 1
        return min_arrow_shots


sol = Solution()
example_points = [[1,2],[3,4],[5,6],[7,8]]
print(sol.findMinArrowShots(example_points))