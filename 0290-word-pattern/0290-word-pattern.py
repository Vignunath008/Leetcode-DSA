class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x={}
        y={}
        w=s.split()
        if len(pattern) != len(w):
            return False
        for i in range(len(pattern)):
            if pattern[i] in x:
                if x[pattern[i]]!=w[i]:
                    return False
            else:
                x[pattern[i]]=w[i]
            if w[i] in y:
                if y[w[i]]!=pattern[i]:
                    return False
            else:
                y[w[i]]=pattern[i]
        return True

                   

                

        