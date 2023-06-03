# Incomplete backtracking solution
from typing import List

class Solution:
    @staticmethod
    def get_coins(su, idx, amount, coins):
        while sum(su) < amount:
            if idx == -1:
                su.pop()
                coins.pop()
                idx = len(coins) -1
            try:
                su.append(coins[idx])
            except:
                return -1
            if sum(su) == amount:
                return len(su)
            if sum(su) > amount:
                if not su:
                    return -1
                su.pop()
                idx -= 1


    def coinChange(self, coins: List[int], amount: int) -> int:
        index = len(coins) - 1
        su = []
        return self.get_coins(su, index, amount, coins)


# Dynamic Programming solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [0] + [amount+1]*amount
        min_coins[0] = 0

        for coin in coins:
            for i in range(1, amount+1):
                if i-coin>=0:
                    min_coins[i]=min(min_coins[i], min_coins[i-coin]+1)
        return -1 if min_coins[-1]==amount+1 else min_coins[-1]
