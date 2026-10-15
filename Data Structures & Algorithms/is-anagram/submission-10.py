class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}
        dictionary2 = {}
        if(len(s) != len(t)):
            return False 
        else:
            for char in s:
                if char in dictionary1:
                    dictionary1[char]+=1
                elif(char not in dictionary1):
                    dictionary1[char] = 1
            for char in t:
                if char in dictionary2:
                    dictionary2[char]+=1
                elif(char not in dictionary2):
                    dictionary2[char]=1
            
        print(dictionary1, dictionary2, dictionary1 == dictionary2)
        return dictionary1 == dictionary2
          
        # return True 
        #     print(i,v)

    
