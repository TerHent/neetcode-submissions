class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(nums)
        print(list(dict.fromkeys(nums)))
        return nums != list(dict.fromkeys(nums))
        