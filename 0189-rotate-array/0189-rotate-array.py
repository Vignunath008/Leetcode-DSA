class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        x=[]
        z=[]
        n=len(nums)
        k%=n
        i=-k
        y=0
        while i<=-1:
            x.append(nums[i])
            i+=1
        while  y<n-k:
            z.append(nums[y])
            y+=1
        nums[:]=x+z

        
        


        