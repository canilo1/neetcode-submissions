class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LeftPointer,RightPointer = 0,1
        maxP = 0
        while RightPointer < len(prices):
            if(prices[LeftPointer]<prices[RightPointer]):
                profit = prices[RightPointer] - prices[LeftPointer]
                maxP = max(maxP,profit)
            else:
                LeftPointer = RightPointer
            RightPointer+=1
        return maxP


        