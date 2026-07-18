class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=[]
        s=list(s)
        t=list(t)
        i=0
        j=0
        while i<len(s) and j<len(t): 
            if s[i]==t[j]:
                x.append(t[j])
                i+=1
                j+=1
            else:
                j+=1
        if s==x:
            return True
        else:
            return False


        