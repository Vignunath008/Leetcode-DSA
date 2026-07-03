class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=[]
        y=[]
        for i in nums:
            if i!=0:
                x.append(i)
            else:
                y.append(i)
        nums[:]=x+y

                
        