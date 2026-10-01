class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize a left pointer, hashmap for count, and a result, and a maxf 
        # moving the right pointer throughout, add the character into the count and update maxf
        # if r - l + 1 - maxf is larger than k, update l and the count for l and update results
        count = {}
        maxf = 0
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf >  k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res


