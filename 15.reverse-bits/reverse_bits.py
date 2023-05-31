
class Solution:
    def reverseBits(self, n: int) -> int:
        num = str(bin(n))[2:]
        num = "0"*(32-len(num)) + num
        rev = num[::-1]
        rev = int(rev, 2)
        return rev
