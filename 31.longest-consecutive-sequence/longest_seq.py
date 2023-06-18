# Brute force solution

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = 0
        curr = 0
        for i in range(min(nums), max(nums)+1):
            if i in nums:
                curr += 1
                if curr > prev:
                    prev = curr
            else:
                curr = 0
        return prev

# Improved solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest