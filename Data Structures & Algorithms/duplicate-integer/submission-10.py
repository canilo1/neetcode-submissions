class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(len(set(nums)),len(nums))
        return len(set(nums)) != len(nums)
        