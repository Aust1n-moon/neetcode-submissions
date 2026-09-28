class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # create a hash set and add all nums to it
    # for i,n in enumerate of the set, if diff = target - num is in set
    # return the i and the index of the num = diff from the set
        m = {}

        for i,n in enumerate(numbers):
            diff = target - n
            if diff in m:
                return [m[diff],i+1]

            m[n] = i+1

        return []


