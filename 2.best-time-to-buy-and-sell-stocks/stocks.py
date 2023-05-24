# Brute-force solution O(n^2) solution
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sofar = 0
        for i, j in enumerate(prices):
            for l in prices[i+1:]:
                if l - j > max_sofar:
                    max_sofar = l-j
        return max_sofar

# Improved solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = max(prices)
        mini = min(prices)
        if prices.index(maxi) > prices.index(mini):
            return maxi - mini
        else:
            max_sofar = 0
            for i, j in enumerate(prices):
                if maxi - j < max_sofar:
                    continue
                if prices[i+1:]:
                    ma = max(prices[i+1:])
                    if ma-j > max_sofar:
                        max_sofar = ma-j
            return max_sofar

# Further improvements

