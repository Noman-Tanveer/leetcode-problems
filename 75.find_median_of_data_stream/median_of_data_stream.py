from collections import heapq as h
class MedianFinder:
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num):
        h.heappush(self.lo, -num)          # lo is maxheap, so -1 * num
        h.heappush(self.hi, -self.lo[0])   # hi is minheap
        h.heappop(self.lo)

        if len(self.lo) < len(self.hi):
            h.heappush(self.lo, -self.hi[0])
            h.heappop(self.hi)

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0] - self.lo[0]) / 2  # - as low has -ve values
