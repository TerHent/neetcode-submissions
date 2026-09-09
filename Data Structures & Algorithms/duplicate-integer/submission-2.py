class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return nums != list(dict.fromkeys(nums))
        