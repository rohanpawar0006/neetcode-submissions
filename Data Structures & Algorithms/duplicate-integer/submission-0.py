class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl = []
        for i in nums:
            if i in dupl:
                return True
            dupl.append(i)
        return False