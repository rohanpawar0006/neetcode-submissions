class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for num in range(1, len(nums)):
            if nums[num] != nums[num - 1]:
                nums[k] = nums[num]
                k += 1
        return k
