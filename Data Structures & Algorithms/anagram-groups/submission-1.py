class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) #for adding operations later

        for s in strs:
            count = [0] * 26 # 1 for each alphabet a-z

            for c in s:
                count[ord(c)-ord("a")] +=1 #get askey btw 0-26 by subtracting "a"
            
            d[tuple(count)].append(s) #for the same count in d, append s in it and operation cant be done in an array so turn into a tuple

        return list(d.values()) #return the list