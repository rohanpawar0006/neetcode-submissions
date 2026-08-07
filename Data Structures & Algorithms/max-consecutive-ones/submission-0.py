class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        best_count = 0
        for i in (nums):
            if i == 1:
                count += 1
                best_count = max(best_count, count)
            else:
                count = 0
        return best_count