# Brute-force solution
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []
        for i in range(len(nums) + 1):
            for j in range(i):
                sums.append(sum(nums[j: i]))
        return max(sums)

# improved solution
