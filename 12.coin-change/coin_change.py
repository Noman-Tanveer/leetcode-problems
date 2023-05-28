# Incomplete backtracking solution
from typing import List

class Solution:
    # def backtrack():
    @staticmethod
    def get_coins(su, idx, amount, coins):
        print(sum(su), amount)
        while sum(su) < amount:
            print(coins, idx)
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
        print(coins[index])
        return self.get_coins(su, index, amount, coins)
