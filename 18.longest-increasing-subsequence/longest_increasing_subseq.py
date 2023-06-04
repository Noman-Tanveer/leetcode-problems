class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		length_of_nums = len(nums)
		cache = [0 for _ in range(length_of_nums)]
		for i in range(1, length_of_nums):
			for j in range(i):
				if nums[j] < nums[i]:
					cache[i] = max(cache[i], cache[j] + 1)
		return max(cache) + 1
