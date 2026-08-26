class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        result = float('inf')

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                result = min(result, (R - L) + 1)
                total -= nums[L]
                L += 1

        return 0 if result == float('inf') else result