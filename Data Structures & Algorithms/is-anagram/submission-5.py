class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(set(s) == set(t)):
            for char in s:
                if(s.count(char)!= t.count(char)):
                    return False
        else:
            return False
        return True
      