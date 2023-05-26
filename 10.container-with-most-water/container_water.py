from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, ans = 0, len(height)-1, 0

        while left <= right:
            ans = max(ans, (right-left) * min(height[right], height[left]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return ans
