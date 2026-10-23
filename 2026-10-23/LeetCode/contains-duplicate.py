class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        sets = set(nums)
        if len(sets) != len(nums):
            return True
        else:
            return False
        