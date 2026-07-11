class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=0
        s=s.rstrip()
        for i in range(len(s)):
            if " " not in s:
                return len(s)

            if s[i]==" ":
                x=max(x,i)
        return len(s[x+1:])
        
        