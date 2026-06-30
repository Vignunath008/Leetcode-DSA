class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        n=len(nums)
        for i in range(n):
            ans=target-nums[i]
            if(ans in s):
                return [s[ans],i]
            s[nums[i]]=i
        return []





        