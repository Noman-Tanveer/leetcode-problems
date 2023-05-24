# Fails for products of negative numbers
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prods = []
        prods.append(nums[0])
        max_prod = prods[0]

        for i in range(1, len(nums)):
            prods.append(max(prods[i-1]*nums[i], nums[i]))
            if prods[i] > max_prod:
                max_prod = prods[i]

        return max_prod

# Improved soution