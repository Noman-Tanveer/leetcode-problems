class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_l = len(s)
        if not s:
            return 0
        if str_l == 1:
            return 1

        ptr1 = 0
        ptr2 = 1
        longest = 1

        while ptr2 < str_l:
            cur = 1
            while ptr2<str_l and s[ptr2] not in s[ptr1:ptr2]:
                ptr2 += 1
                cur = ptr2-ptr1
            else:
                longest = cur if cur > longest else longest
                ptr1 += 1
                ptr2 = ptr1+1
        return longest
