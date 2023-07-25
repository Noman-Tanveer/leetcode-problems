class Solution:
    def longestPalindrome(self, s: str) -> str:

        largest = ""
        i = 0
        while i+len(largest) <= len(s):
            j = i+len(largest)
            while j <= len(s):
                if s[i:j] == s[i:j][::-1]:
                    largest = s[i:j] if len(s[i:j])>len(largest) else largest
                j += 1
            i += 1
        return largest
