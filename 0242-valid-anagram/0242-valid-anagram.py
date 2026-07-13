class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        x={}
        y={}
        for i in s:
            x[i]=x.get(i,0)+1
        for j in t:
            y[j]=y.get(j,0)+1
        return x==y
        

        