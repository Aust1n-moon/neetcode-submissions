class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}

        if len(s) != len(t):
            return False
        
        else:
            for i in s:
                if i in d:
                    d[i] +=1
                else:
                    d[i] = 1


            for j in t:
                if j in d2:
                    d2[j] +=1
                else:
                    d2[j] = 1

            if d == d2:
                return True
        
        return False