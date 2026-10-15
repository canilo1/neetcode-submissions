class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Sum = 0
        LP = 0
        RP = len(numbers)-1
        while LP!= RP:
            Sum = numbers[LP] + numbers[RP]
            
            if(Sum<target):
                print("This is the Sum less than target",Sum)
                LP+=1
            else:
                if(Sum == target):
                    break
                print("This is the sum greater than target",Sum)
                RP-=1
        return[LP+1,RP+1]


        