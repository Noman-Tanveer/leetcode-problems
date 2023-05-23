import math
import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            numbers = copy.deepcopy(nums)
            numbers.remove(i)
            arr.append(math.prod(numbers))
        return arr
        
# Improved solution

