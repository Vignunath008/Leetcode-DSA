class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x={}
        y={}
        for i in range(len(s)):
            if s[i] in x:
                if x[s[i]]!=t[i]:
                    return False
            else:
                x[s[i]]=t[i]
            if t[i] in y:
                if y[t[i]]!=s[i]:
                    return False
            else:
                y[t[i]]=s[i]
        return True

        