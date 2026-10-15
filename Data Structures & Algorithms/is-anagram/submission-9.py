class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False
        s = sorted(s)
        t = sorted(t)
        Counter = 0 
        while Counter<len(s):
            if(s[Counter]!= t[Counter]):
                return False
            else:
                Counter+=1
        return True