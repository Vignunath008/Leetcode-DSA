class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        maxi=0
        for i in nums:
            freq[i]=freq.get(i,0)+1 
        return max(freq, key=freq.get)
        