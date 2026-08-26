class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        hashSet =set()
        result = 0
        for R in range(len(s)):
            while s[R] in hashSet:
                hashSet.remove(s[L])
                L += 1
            hashSet.add(s[R])
            result = max(result, R - L + 1)
        return result