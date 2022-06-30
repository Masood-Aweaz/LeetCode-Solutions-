class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        set_l = len(set(nums))
        if l == set_l:
            return False
        return True
