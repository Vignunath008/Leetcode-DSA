class Solution:
    def isValid(self, s: str) -> bool:
        x={"(":0,"[":1,"{":2}
        y={")":0,"]":1,"}":2}
        z=[]
        for i in range(len(s)):
            if s[i] in x:
                z.append(x[s[i]])
            elif s[i] in y:
                if not z:
                    return False
                elif z[-1]!=y[s[i]]:
                    return False
                else:
                    z.pop()
        if not z:
            return True
        else:
            return False
        
                

            

        