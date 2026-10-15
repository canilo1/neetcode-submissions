class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Understand:
            It can only be one pair that adds to one thing,  the target
        Plan:
        Sort the Array first
        [1,5,3,2,1] => [1,1,2,3,5] target = 8
        Initlize a dictonary 
        Get a loop that stores the index and the number aswell
            Add it to the dictonary(Key being the number, value being the index)
            Get the x(the value that would sum it to the target) by target-number
            we check if the target is in the array, then if it is we will then  we will index and get 
            the index or so 

        '''
        dictonary = {}
        for index, numbers in enumerate(nums):
            complement = target - numbers
            if complement in dictonary:
                return [dictonary[complement], index]
            dictonary[numbers] = index
          


'''

'''






