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
# Dynamic programming
class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums):
                if must_pick:
                    return 0
                else:
                    return -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)
