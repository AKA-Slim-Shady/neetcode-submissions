class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        h = {}

        for i in words:
            for j in i:
                if j not in h:
                    h[j] = 1
                else:
                    h[j] += 1
        
        for i in h:
            if h[i] % len(words) != 0:
                return False

        return True
        



