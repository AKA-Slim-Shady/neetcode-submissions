class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h = {}

        for i in arr:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        
        comp = -1
        for i in h:
            if h[i] == i:
                comp = max(comp , i)
        
        return comp