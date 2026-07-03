class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[]
        for i in range(rowIndex+1):
            row=[1]
            if i>0:
                prev=result[-1]
                for j in range(1,i):
                    row.append(prev[j-1]+prev[j])
                row.append(1)
            result.append(row)
        return result[-1]
        