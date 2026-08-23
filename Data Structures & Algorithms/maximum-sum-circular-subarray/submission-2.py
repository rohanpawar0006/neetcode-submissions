class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSub = nums[0]
        maxSub = nums[0]
        minCurr, maxCurr = 0, 0
        total = 0
        for i in nums:
            minCurr = min(i, minCurr + i)
            minSub = min(minCurr, minSub)
            maxCurr = max(i, maxCurr + i)
            maxSub = max(maxCurr, maxSub)
            total += i
        if minSub == total:
            return maxSub
        else:
            return max(maxSub, total - minSub)