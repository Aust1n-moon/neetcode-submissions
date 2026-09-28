class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        count = 0
        best = 0

        for n in nums:
            seen.add(n)

        for n in seen:
            if n-1 not in seen:
                count = 1
                while (n+count) in seen:
                    count +=1
                best = max(best, count)

        return best