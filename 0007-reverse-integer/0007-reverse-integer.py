class Solution:
    def reverse(self, x: int) -> int:
        z=str(abs(x))
        y=z[::-1]
        if x!=abs(x):
            ans=-abs(int(y))
        else:
            ans=int(y)
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        return ans
            



            
            
        