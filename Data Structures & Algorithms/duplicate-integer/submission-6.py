from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Understand:
            If all elements are unique, return True.
            If there is any duplicate, return False.

        Plan:
            Loop through the array using the count method.
            If any number appears more than once, return False.
            If loop finishes without finding duplicates, return True.
        '''
        for numbers in nums:
            if(nums.count(numbers)>1):
                return True
        return False