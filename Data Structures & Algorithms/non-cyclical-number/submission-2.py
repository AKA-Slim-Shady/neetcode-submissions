class Solution:
    def isHappy(self, n: int) -> bool:
        
        h = {}

        s = 0
        n = list(str(n))

        while True:
            s = sum([(int(i)**2) for i in n])
            
            if s == 1 and s not in h:
                return True
            if s not in h:
                h[s] = 1
                n = list(str(s))
                continue
            if s in h:
                return False
