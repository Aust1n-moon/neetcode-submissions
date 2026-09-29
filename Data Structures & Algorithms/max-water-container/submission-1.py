class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        # set a maxwater and using two pointer, one from l and one from right
        # compute water = (l - r) x whichever height is lower
        # if water > maxwater, replace maxwater with water
        #return maxwater at the end
        maxwater = 0

        l, r = 0 , len(heights)-1

        while l < r:
                
            if heights[l] <= heights[r]:
                water = (r - l) * heights[l]
                l += 1
                
            elif heights[r] <= heights[l]:
                water = (r - l) * heights[r]
                r -= 1
                
            if water >= maxwater:
                maxwater = water

        return maxwater


            
        