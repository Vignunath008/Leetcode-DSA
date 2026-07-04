class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        freq={}
        l=0
        h=n-1
        mid=(l+h)//2
        y=nums[mid]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        if freq[y]==1:
            return True
        else:
            return False

        