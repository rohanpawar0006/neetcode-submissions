class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSub = nums[0]
        maxSub = nums[0]
        minCurr, maxCurr = nums[0], nums[0]
        total = sum(nums)
        for i in range(1, len(nums)):
            minCurr = min(nums[i], minCurr + nums[i])
            minSub = min(minCurr, minSub)
            maxCurr = max(nums[i], maxCurr + nums[i])
            maxSub = max(maxCurr, maxSub)
            
        if minSub == total:
            return maxSub
        else:
            return max(maxSub, total - minSub)