class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        cache = [0]* (n+1)
        # base case
        cache[0] = 1
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                cache[i] = cache[i - 1]
            if i >= 2:
                x = int(s[i - 2: i])
                if 10 <= x <= 26:
                    cache[i] += cache[i - 2]
        return cache[n]


# Faster solution
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        cache = [0]*(n+1)
        cache[0] = 1

        for i in range(1, n+1):
            if s[i-1] != "0":
                cache[i] = cache[i-1]

            if i>=2 and (int(s[i-2:i]) in range(10,27)):
                cache[i] += cache[i-2]
        return cache[-1]
