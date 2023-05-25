import math
import copy
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            numbers = copy.deepcopy(nums)
            numbers.remove(i)
            arr.append(math.prod(numbers))
        return arr

# Improved solution
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1]*(len(nums))
        post_prod = [1]*(len(nums))
        prod = [1]*(len(nums))
        leftp = 1
        rightp = 1

        for i in range(len(nums)):
            pre_prod[i] = leftp
            leftp *= nums[i]

        for j in range(len(nums)-1, -1, -1):
            post_prod[j] = rightp
            rightp *= nums[j]

        prod[0] = post_prod[0]
        prod[len(nums)-1] = pre_prod[len(nums)-1]

        for i in range(1, len(nums)-1):
            prod[i] = pre_prod[i]*post_prod[i]

        return prod
