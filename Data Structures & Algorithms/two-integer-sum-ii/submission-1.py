class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # two pointer approach
    # count up from bottom and count down from the end
    # and when reaching a index pair that adds up to target, add 1 to them and return

        l, r = 0, len(numbers) -1

        while l < r:
            cursum = numbers[l] + numbers[r]

            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []


        

