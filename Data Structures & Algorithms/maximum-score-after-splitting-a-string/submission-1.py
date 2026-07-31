class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(1 , len(s)):
            l_sub = s[:i]
            r_sub = s[i:]
            lz = 0
            for i in l_sub:
                if i == "0":
                    lz += 1
            ro = 0
            for i in r_sub:
                if i == "1":
                    ro += 1
            
            score = max(score , lz+ro)
            
        return score