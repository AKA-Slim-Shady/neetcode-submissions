class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False
        h = {}
        ch = {}
        
        for c , w in zip(pattern , words):
            if w not in h:
                h[w] = c
            if h.get(w) != c :
                return False
            
            if c not in ch:
                ch[c] = w
            if ch.get(c) != w:
                return False 

                
        
        print(h)
        return True

