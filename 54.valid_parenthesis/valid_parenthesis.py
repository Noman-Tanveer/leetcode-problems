class Solution:
    def isValid(self, s: str) -> bool:
        pars = {')': '(', '}':'{', ']':'['}
        stack = []
        if len(s) % 2:
            return False

        for i in s:
            if i in pars.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == pars[i]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        return False
