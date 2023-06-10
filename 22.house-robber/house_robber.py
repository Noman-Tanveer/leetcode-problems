from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        cache[0] = nums[0]
        if len(nums) == 1:
            return cache[0]
        cache[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cache[i] = max(cache[i-1], cache[i-2]+nums[i])
        return cache[-1]
