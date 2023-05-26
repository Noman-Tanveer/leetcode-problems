# A simple solution without taking benefit of sorting
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

# Improved solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + int((right - left) / 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
