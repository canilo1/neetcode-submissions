class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        LP = 0
        RP = len(numbers)-1
        print("This is RP",RP,numbers[RP])
        while LP<RP:
            if(numbers[LP] + numbers[RP]>target):
                RP-=1
            elif(numbers[LP]+numbers[RP]<target):
                LP+=1
            else:
                return [LP+1,RP+1]

