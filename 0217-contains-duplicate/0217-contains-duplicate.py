class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for y in freq:
            if freq[y]>1:
                return True
                break
        return False
        
        