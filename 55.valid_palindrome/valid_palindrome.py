class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ne_s = ""
        for i in s:
            ne_s += i if i.isalnum() else ""
        return ne_s[:len(ne_s)//2] == ne_s[::-1][:len(ne_s)//2]
