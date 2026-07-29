class Solution:
    def scoreOfString(self, s: str) -> int:
        val = 0
        comp = []
        for i in s:
            t = ord(i)
            comp.append(t)
        
        left = 0
        for right in range(1 , len(comp)):
            diff = abs(comp[right] - comp[left])
            val += diff
            left += 1
        
        return val
