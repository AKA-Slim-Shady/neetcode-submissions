class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        print(g , s)
        
        ret = 0
        s_ptr = 0
        g_ptr = 0

        while g_ptr < len(g) and s_ptr < len(s):
            if g[g_ptr] <= s[s_ptr]:
                ret += 1
                g_ptr += 1
            s_ptr += 1

        return ret