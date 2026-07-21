class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        ans=[1]*n
        product=1
        for i in range(n):
            prefix[i]=product
            product*=nums[i]
        product=1
        for j in range(n-1,-1,-1):
            suffix[j]=product
            product*=nums[j]
        for z in range(n):
            ans[z]=prefix[z]*suffix[z]
        return ans


        