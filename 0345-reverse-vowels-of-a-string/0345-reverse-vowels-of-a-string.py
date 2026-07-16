class Solution:
    def reverseVowels(self, s: str) -> str:
        x=["a","e","i","o","u"]
        y=[]
        for i in s:
            if i.lower() in x:
                y.append(i)
        y[:]=y[::-1]
        i=0
        r=0
        s=list(s)
        while i<len(s):
            if s[i].lower() in x:
                s[i]=y[r]
                i+=1
                r+=1
            else:
                i+=1
        return "".join(s)

            
        