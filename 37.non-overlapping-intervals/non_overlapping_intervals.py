# Simple solution
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Needs to be done with dynamic programming
        std_itvls = sorted(intervals, key=lambda x: x[1]*10+x[0])
        removed = 0
        selected = [std_itvls[0]]
        for i in std_itvls[1:]:
            if i[0] >= selected[-1][-1]:
                selected.append(i)
            else:
                removed += 1
        return removed

# Reduced Memory usage
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        std_itvls = sorted(intervals, key=lambda x: x[1])
        removed = 0
        selected = std_itvls[0][-1]
        for i in std_itvls[1:]:
            if i[0] < selected:
                removed += 1
            else:
                selected = i[-1]
        return removed
