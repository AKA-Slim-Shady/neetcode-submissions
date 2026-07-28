class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        if len(s) != len(t):
            return False;
        for i in s:
            if i in dict1:
                s = dict1[i]
                s = s+1
                dict1[i] = s
            else:
                dict1[i] = 1;
        for i in t:
            if i in dict2:
                s = dict2[i]
                s = s+1
                dict2[i] = s
            else:
                dict2[i] = 1;
        print(dict1)
        print(dict2)
        if dict1 != dict2:
            return False;
        return True