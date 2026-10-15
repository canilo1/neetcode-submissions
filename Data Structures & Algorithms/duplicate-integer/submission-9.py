class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        Counter = 0 
        while Counter<len(nums):
            if(nums[Counter] in freq):
                return True
            else:
                freq[nums[Counter]] = 1
                Counter+=1
        return False
        