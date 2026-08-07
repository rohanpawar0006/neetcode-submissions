class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(low, high):
            pivot, point = nums[high], low
            for i in range(low, high):
                if nums[i] <= pivot:
                    nums[point], nums[i] = nums[i], nums[point]
                    point += 1
            nums[point], nums[high] = nums[high], nums[point]
            if point > k:   return quickSelect(low, point - 1)
            elif point < k: return quickSelect(point + 1, high)
            else:           return nums[point]
        return quickSelect(0, len(nums) - 1)