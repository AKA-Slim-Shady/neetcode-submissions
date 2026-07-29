class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        rows = [[1] , [1 , 1]]

        while True:
            if len(rows) - 1 < rowIndex:
                row = rows[-1]
                left = 0
                temp = []
                temp.append(row[left])
                for right in range(1 , len(rows)):
                    temp.append(row[right]+row[left])
                    left += 1
                temp.append(row[-1])
                rows.append(temp)
            else:
                return rows[-1]
                break