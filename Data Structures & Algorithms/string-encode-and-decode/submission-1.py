class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for i in strs:
            res += str(len(i))
            res += ":"
            res += i
        return res

    def decode(self, s: str) -> List[str]:
    # create a result array
    # for every character in s, add to an empty string, if its ":", skip and add to the index if its a proper string
        
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i = j
        
        return res
