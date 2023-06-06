# Incorrect solution does take into account the order of letters in strings

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lens = [[0] * (len(text1))] * len(text2)
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text2[j] == text1[i]:
                    lens[j][i] = max(lens[j-1][i], lens[j][i-1]) + 1
                else:
                    lens[j][i] = max(lens[j-1][i], lens[j][i-1])
        return lens[-1][-1]

