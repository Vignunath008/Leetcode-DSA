class Solution:
    def isValid(self, s: str) -> bool:
        y={"(":0,"[":1,"{":2}
        x={")":0,"]":1,"}":2}
        z=[]
        for i in range(len(s)):
            if s[i] in y:
                z.append(y[s[i]])
            elif s[i] in x:
                if not z:
                    return False
                if z[-1]!=x[s[i]]:
                    return False
                else:
                    z.pop()
        if not z:
            return True
        else:
            return False
        
            
            

            

        