from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + str(len(i)) + "~" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        num = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
                i += 1
            elif s[i] == "~":
                length = int(num)
                start = i + 1
                end = start + length
                sstr = s[start:end]
                ans.append(sstr)
                i = end  # move i to the end of current string
                num = ""
            else:
                i += 1
        return ans

def main():
    sol = Solution()
    encoded = sol.encode(["1,23", "45,6", "7,8,9"])
    print("Encoded:", encoded)
    print("Decoded:", sol.decode(encoded))

main()
