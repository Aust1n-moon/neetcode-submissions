class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #edge cases: 2 zeros, 2 of the same nmbers
        prod, num_zeros = 1,0

        for num in nums:
            if num:
                prod *= num
            else:
                num_zeros +=1
        
        if num_zeros > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i,n in enumerate(nums):
            if num_zeros: res[i] = 0 if n else prod
            else:
                res[i] = prod // n
        
        return res
        