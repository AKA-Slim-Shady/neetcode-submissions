class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + i + "~"
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        for i in s.split("~"):
            ans.append(i)
        ans.pop()
        return ans

def main():
    sol = Solution()
    print(sol.encode(["neet", "code", "love", "you"]))

main()
