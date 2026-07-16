class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
       
        n=len(nums)    
        def fun(i,count,expected):
            if i == n - 1:
                return count
            if nums[i+1]-nums[i]==expected:
                return fun(i+1,count+1,-expected)
            return count
        maxi=-1
        for i in range(n-1):
            if nums[i+1]-nums[i]==1:
                maxi=max(maxi,fun(i+1,2,-1))
        
        return maxi



        