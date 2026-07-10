class Solution:
    def romanToInt(self, s: str) -> int:
        total=0
        x={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            if i<len(s)-1 and x[s[i]]<x[s[i+1]]:
                total-=x[s[i]]
            else:
                total+=x[s[i]]
        return total
                
            
        