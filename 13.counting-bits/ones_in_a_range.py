from typing import List

class Solution:
    @staticmethod
    def count(i):
        k = 0
        while i>=1:
            k += i%2
            i = i >> 1
        return k
    def countBits(self, n: int) -> List[int]:
        lis = []
        for i in range(n+1):
            lis.append(self.count(i))
        return lis
