class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = { ")":"(", "}":"{", "]":"["}
        stack = []
        for par in s:
            if par in hashMap:
                if stack and stack[-1] == hashMap[par]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(par)

        return True if not stack else False
