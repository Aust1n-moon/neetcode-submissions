class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using a two pointer
        # count up from left and count down from right
        # create a sorted list first, and for each index, disregard that one and use two pointers to check all other pairs + the index number that adds up to 0

        nums.sort()

        res = []

        for i,n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i+1, len(nums) -1


            while l < r:
                cursum = n + nums[l] + nums[r]

                if (cursum < 0):
                    l += 1
                elif (cursum > 0):
                    r -= 1
                elif cursum == 0:
                    res.append([n, nums[l], nums[r]])
                    l+= 1
                    r-= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return res