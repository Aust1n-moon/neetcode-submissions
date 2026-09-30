class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # count up r and add 1 to res until dupe is seen, then move l to r, compare maxs and res, and replace if res > maxs
        # reset res to 0
        # add 1 to r
        
        char = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            res = max(res, r - l + 1)
        
        return res

 



