class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=""
        ls=[]
        for i in digits:
            x+=str(i)
        y=int(x)
        y+=1
        for m in str(y):
            ls.append(m)
            ls=[int(x) for x in ls]
        return ls
        

        