from typing import List

# A simple solution with exploiting array being sorted/rotated
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1

# Improved solution
