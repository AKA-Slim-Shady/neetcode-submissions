class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0

        for i in logs:
            if "/" in i and "./" not in i and "../" not in i:
                count += 1
            elif "../" in i and count != 0:
                count -= 1
        
        return count