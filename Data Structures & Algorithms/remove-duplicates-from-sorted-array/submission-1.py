class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)
        for num in range(1, n):
            if nums[num] != nums[num - 1]:
                nums[k] = nums[num]
                k += 1
        return k
