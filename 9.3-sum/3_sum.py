# Brute-force solution
from itertools import combinations
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        combs = list(combinations(nums, 3))
        for i in combs:
            if sum(i) == 0:
                n_lis = sorted(list(i))
                if n_lis not in triplets:
                    triplets.append(n_lis)
        return list(triplets)

# Using two pointer approach
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        std_nums = sorted(nums)
        triplets = set()
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                p_sum = std_nums[i] + std_nums[j] + std_nums[k]
                # print(p_sum, "::", std_nums[i], std_nums[j], std_nums[k])
                if p_sum == 0:
                    triplets.add((std_nums[i], std_nums[j], std_nums[k]))
                    j += 1
                    k -= 1
                elif p_sum < 0:
                    j += 1
                else:
                    k -= 1

        return list(triplets)