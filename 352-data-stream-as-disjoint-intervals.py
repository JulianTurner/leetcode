from sortedcontainers import SortedDict

class SummaryRanges:

    def __init__(self):
        '''SummaryRanges() Initializes the object with an empty stream.'''
        self.num_intervals = SortedDict()

    def addNum(self, value: int) -> None:
        '''Adds the integer value to the stream.'''
        if value in self.num_intervals:
            return

        expectation = [value, value]

        if (value + 1) in self.num_intervals:
            above_item = self.num_intervals.pop(value + 1)
            expectation[1] = above_item[1]

        current_keys = self.num_intervals.keys()
        insertion_point = self.num_intervals.bisect_left(value)
        if insertion_point != 0:
            smaller_key = current_keys[insertion_point-1]
            smaller_value = self.num_intervals[smaller_key]
            if smaller_value[0] <= value <= (smaller_value[1] + 1):
                smaller_value[1] = max(smaller_value[1], expectation[1])
                self.num_intervals[smaller_key] = smaller_value
            else:
                self.num_intervals[value] = expectation
        else:
            self.num_intervals[value] = expectation

    def getIntervals(self) -> list[list[int]]:
        '''Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by start i.'''
        return list(self.num_intervals.values())


# Your SummaryRanges object will be instantiated and called as such:
summaryRanges = SummaryRanges()
summaryRanges.addNum(1)  # arr = [1]
print(summaryRanges.getIntervals())  # return [[1, 1]]
summaryRanges.addNum(3)  # arr = [1, 3]
print(summaryRanges.getIntervals())  # return [[1, 1], [3, 3]]
summaryRanges.addNum(7)  # arr = [1, 3, 7]
print(summaryRanges.getIntervals())  # return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2)  # arr = [1, 2, 3, 7]
print(summaryRanges.getIntervals())  # return [[1, 3], [7, 7]]
summaryRanges.addNum(6)  # arr = [1, 2, 3, 6, 7]
print(summaryRanges.getIntervals())  # return [[1, 3], [6, 7]]