class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer approach
        # if seen a wall taller on either side, update the other sides pointer, then take the max from the previous highest of that side and the height of that side its currently in,and if the new one is higher, add the difference to the result

        if not height:
            return 0
            
        l,r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        res = 0

        while l < r:
            if leftmax <  rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
            
        return res


