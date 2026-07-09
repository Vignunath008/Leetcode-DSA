class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        count=0
        for i in nums:
            if i!=1:
                count=0
            else:
                count+=1
                maxi=max(count,maxi)

        return maxi


        