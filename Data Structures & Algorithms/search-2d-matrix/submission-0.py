class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        for row in matrix:
            if self.binarySearch(row, target):
                return True
        return False
    def binarySearch(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
            else:
                return True
        return False
