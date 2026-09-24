class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        s = sorted(count.items(), key=lambda x: x[1])

        res = []
        while range(len(s) > k):
            s.pop(0)
        
        for n in s:
            res.append(n[0])

        return res

