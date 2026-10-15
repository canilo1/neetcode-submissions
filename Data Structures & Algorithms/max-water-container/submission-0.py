class Solution:
    def maxArea(self, heights: List[int]) -> int:
        LP = 0
        RP = len(heights)-1
        Sum = 0
        while LP != RP:
            maxWater = abs((LP-RP)*min(heights[LP],heights[RP]))
            print('This is maxWater',maxWater)
            if(maxWater>Sum):
                Sum = maxWater
            if(heights[LP]<heights[RP]):
                LP+=1
            else:
                RP-=1
        return Sum

            


        