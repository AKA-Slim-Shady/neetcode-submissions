class Solution:
    def generateChildren(self , lock: str) -> List[str]:
        res = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            new = lock[:i] + digit + lock[i+1:]
            res.append(new)
            digit = str(((int(lock[i]) - 1) + 10) % 10)
            new = lock[:i] + digit + lock[i+1:]
            res.append(new)
        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        visited = set(deadends)

        q = deque()

        q.append(["0000" , 0])

        while q:
            child , count  = q.popleft()
            if child == target:
                return count
            
            for i in self.generateChildren(child):
                if i not in visited:
                    q.append([i , count + 1])
                    visited.add(i)
                    
                

        
        return -1

        