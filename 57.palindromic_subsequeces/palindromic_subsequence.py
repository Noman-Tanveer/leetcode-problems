class Solution:
    def expand_and_count(self, i, j, s):
        length=len(s)
        cnt=0

        while 0<=i and j<length and s[i]==s[j]:
            i-=1
            j+=1
            cnt+=1

        return cnt

    def countSubstrings(self, s: str) -> int:
        return sum(self.expand_and_count(i, i, s) + self.expand_and_count(i, i+1, s) for i in range(len(s)))
