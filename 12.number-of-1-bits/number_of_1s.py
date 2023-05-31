
class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 1
        if n == 0:
            return 0
        while n > 2:
            n, r = divmod(n, 2)
            if r:
                k+=1
        return k
