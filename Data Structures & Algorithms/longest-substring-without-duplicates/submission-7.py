class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        SlidingWindow = []
        maxCounter = 0
        for index,char in enumerate(s):
           
            while(char in SlidingWindow):
                SlidingWindow.pop(0)
        
            SlidingWindow.append(char)
            maxCounter = max(maxCounter,len(SlidingWindow))
        return maxCounter