class Solution:
    def rob(self, nums: List[int]) -> int:
        cache1 = [0] * (len(nums))
        cache2 = [0] * (len(nums))
        if len(nums) <= 3:
            return max(nums)
        cache1[0] = nums[0]
        cache1[1] = max(nums[1], nums[0])
        cache2[0] = nums[1]
        cache2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums)-1):
            cache1[i] = max(cache1[i-1], cache1[i-2]+nums[i])

        for i in range(3, len(nums)):
            cache2[i] = max(cache2[i-1], cache2[i-2]+nums[i])

        print(cache1, cache2)

        return max(max(cache1[-2:]), max(cache2[-2:]))
