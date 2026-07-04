class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        freq={}
        mid=nums[n//2]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        if freq[mid]==1:
            return True
        else:
            return False

        